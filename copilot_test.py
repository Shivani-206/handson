import os
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
            output = subprocess.check_output("net stats srv", shell=True, text=True)
            for line in output.splitlines():
                if "Statistics since" in line:
                    print(f"System uptime (since): {line.split('since', 1)[1].strip()}")
                    break
        elif system == "Linux":
            # Use /proc/uptime
            with open("/proc/uptime", "r") as f:
                uptime_seconds = float(f.readline().split()[0])
                hours = int(uptime_seconds // 3600)
                minutes = int((uptime_seconds % 3600) // 60)
                seconds = int(uptime_seconds % 60)
                print(f"System uptime: {hours}h {minutes}m {seconds}s")
        elif system == "Darwin":
            # macOS: use 'uptime' command
            output = subprocess.check_output("uptime", shell=True, text=True)
            print(f"System uptime: {output.strip()}")
        else:
            print("Unsupported operating system for uptime retrieval.")
    except Exception as e:
        print(f"Error retrieving uptime: {e}")

if __name__ == "__main__":
    print_system_uptime()
