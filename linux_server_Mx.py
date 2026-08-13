#!/usr/bin/env python3
import shutil
import psutil
import subprocess
import os
from datetime import datetime

# --- CONFIGURATION ---
# Set thresholds and services you want to actively monitor
DISK_THRESHOLD_PCT = 85.0
CPU_THRESHOLD_PCT = 80.0
MEMORY_THRESHOLD_PCT = 85.0
CRITICAL_SERVICES = ["ssh", "cron", "nginx"]  # Change to your actual service names
LOG_FILE_PATH = "/var/log/server_management.log" # Requires sudo, or change to a home dir path

def log_message(level, message):
    """Formats and writes administrative logs to the designated file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_line = f"[{timestamp}] [{level.upper()}] {message}\n"
    print(formatted_line.strip()) # Print to console
    
    try:
        with open(LOG_FILE_PATH, "a") as f:
            f.write(formatted_line)
    except PermissionError:
        print(f"[ERROR] Cannot write to {LOG_FILE_PATH}. Run with sudo or update path.")

def check_disk_space():
    """Monitors the root filesystem usage."""
    total, used, free = shutil.disk_usage("/")
    used_pct = (used / total) * 100
    if used_pct >= DISK_THRESHOLD_PCT:
        log_message("CRITICAL", f"Low disk space on root (/). Used: {used_pct:.2f}%")
    else:
        log_message("INFO", f"Disk space healthy. Used: {used_pct:.2f}%")

def check_system_resources():
    """Tracks overall CPU and RAM loads."""
    cpu_pct = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    
    if cpu_pct >= CPU_THRESHOLD_PCT:
        log_message("WARNING", f"High CPU utilization detected: {cpu_pct}%")
    else:
        log_message("INFO", f"CPU load stable: {cpu_pct}%")
        
    if memory.percent >= MEMORY_THRESHOLD_PCT:
        log_message("CRITICAL", f"High RAM usage detected: {memory.percent}%")
    else:
        log_message("INFO", f"Memory usage stable: {memory.percent}%")

def check_services():
    """Verifies if systemd services are actively running."""
    for service in CRITICAL_SERVICES:
        try:
            # Executes systemctl check
            result = subprocess.run(
                ["systemctl", "is-active", service], 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                text=True
            )
            status = result.stdout.strip()
            if status == "active":
                log_message("INFO", f"Service '{service}' is running.")
            else:
                log_message("CRITICAL", f"Service '{service}' is DOWN (Status: {status}). Attempting restart...")
                restart_service(service)
        except FileNotFoundError:
            log_message("ERROR", "systemctl command not found. Script might not be running on systemd Linux.")
            break

def restart_service(service_name):
    """Attempts to auto-heal a failed service."""
    # Note: This requires the script to run with sudo privileges
    result = subprocess.run(["sudo", "systemctl", "restart", service_name], stderr=subprocess.PIPE)
    if result.returncode == 0:
        log_message("INFO", f"Successfully restarted service '{service_name}'.")
    else:
        log_message("ERROR", f"Failed to restart service '{service_name}'. Error: {result.stderr.decode().strip()}")

def main():
    log_message("INFO", "=== Starting Server Management Check ===")
    
    # Run core routines
    check_disk_space()
    check_system_resources()
    check_services()
    
    log_message("INFO", "=== Server Management Check Completed ===")

if __name__ == "__main__":
    # Ensure dependencies exist
    # Quick fix if missing: pip install psutil
    main()
