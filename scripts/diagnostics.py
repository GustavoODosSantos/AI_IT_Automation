import os
import platform
import socket
import json
import psutil
import time
from datetime import datetime

def collect_system_info():
    """Collects basic information for diagnostics."""
    info = {
        "os_name": platform.system(),
        "os_version": platform.version(),
        "current_user": os.getlogin(),
        "uptime_seconds": round(time.time() - psutil.boot_time(), 2),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage('/').percent,
        "ip_address": socket.gethostbyname(socket.gethostname()),
    }
    return info

def save_report(info):
    """Save system info to JSON File."""
    with open("system_report.json", "w") as f:
        json.dump(info, f, indent=4)

def log_execution():
    """Append execution time to diagnostics.log."""
    with open("diagnostics.log", "a") as log:
        log.write(f"Diagnostics run at {datetime.now()}\n")

if __name__ == "__main__":
    print("[START] Script started")
    system_info = collect_system_info()
    save_report(system_info)
    log_execution()
    print(" System report generated successfully!")