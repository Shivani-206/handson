import platform
import subprocess

def print_system_uptime():
    """
    Prints the system uptime in a cross-platform way.
    """
    system = platform.system()
    try:
        if system == "Windows":
            # Use 'net stats srv' and parse output
            result = subprocess.run(
                ["net", "stats", "srv"],
                capture_output=True,
                text=True,
                check=True
            )
            for line in result.stdout.splitlines():
                if "Statistics since" in line:
                    print(f"System uptime (since): {line.split('since', 1)[1].strip()}")
                    break
        elif system == "Linux":
            # Use /proc/uptime
            try:
                with open("/proc/uptime", "r") as f:
                    uptime_seconds = float(f.readline().split()[0])
                    hours = int(uptime_seconds // 3600)
                    minutes = int((uptime_seconds % 3600) // 60)
                    seconds = int(uptime_seconds % 60)
                    print(f"System uptime: {hours}h {minutes}m {seconds}s")
            except OSError as e:
                print(f"Error opening /proc/uptime: {e}")
        elif system == "Darwin":
            # macOS: use 'uptime' command
            result = subprocess.run(
                ["uptime"],
                capture_output=True,
                text=True,
                check=True
            )
            print(f"System uptime: {result.stdout.strip()}")
        else:
            print("Unsupported operating system for uptime retrieval.")
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
    except Exception as e:
        print(f"Error retrieving uptime: {e}")

if __name__ == "__main__":
    print_system_uptime()
