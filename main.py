import psutil 
import time 
import os

def display_dashboard():
    border = "=" * 50
    text = "SYSTEM MONITOR DASHBOARD"
    print(border)
    print(f"{text: ^50}") # Center-aligned with `-`
    print(border)
    print()


    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"{'CPU Usage:':<25}{cpu_usage}%")

    memory_usage = psutil.virtual_memory().percent
    print(f"{'Memory Usage:':<25}{memory_usage}%")

    disk_space_taken = psutil.disk_usage('/').percent
    print(f"{'Disk Usage:':<25}{disk_space_taken}%")

def clear_dashboard():
    os.system('clear')

while True:
    clear_dashboard()
    display_dashboard()
    time.sleep(2)
    
