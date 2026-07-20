import psutil 
import time 
import os
import colorama
from colorama import Fore, Style, init

init()

def display_dashboard():
    border = Style.BRIGHT + Fore.BLUE + "=" * 50 + Style.RESET_ALL
    text ="SYSTEM MONITOR DASHBOARD"
    print(border)
    print(Style.BRIGHT + Fore.BLUE + f"{text:^50}" + Style.RESET_ALL)
    print(border)
    print()

    memory_usage = psutil.virtual_memory().percent
    print(f"{'Memory Usage:':<25}{memory_usage}%" )

    disk_space_taken = psutil.disk_usage('/').percent
    print(f"{'Disk Usage:':<25}{disk_space_taken}%")
    print()

    cpu_usage = psutil.cpu_percent(interval=0)
    cpu_usage_color = cpu_color(cpu_usage)
    print(f"{'CPU Usage:':<25}"
          f"{cpu_usage_color}{cpu_usage}%{Style.RESET_ALL}")
    
    cpu_level = cpu_status(cpu_usage)
    print(f"{'CPU Level:':<25}"
          f"{cpu_usage_color}{cpu_level}{Style.RESET_ALL}")
    print()

    highest = 0
    top_process = None
    for process in psutil.process_iter(['name', 'cpu_percent']):
        try:
            cpu = process.info['cpu_percent']

            if cpu is not None and cpu > highest:
              highest = cpu
              top_process = process

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    print(
     f"{'Top Process:':<25}{top_process.info['name']} ({highest}%)"
     if top_process else "No processes found"
    )       
    
def cpu_status(cpu_usage):

    if cpu_usage <= 50:
        return "Low"
    elif cpu_usage <= 80:
        return "Moderate" 
    else:
        return "High" 
    
def cpu_color(cpu_usage):
    if cpu_usage <= 50:
        return Fore.GREEN 
    elif cpu_usage <= 80:
        return Fore.YELLOW 
    else:
        return Fore.RED 
    
    

def clear_dashboard():
    os.system('clear')

while True:
    clear_dashboard()
    display_dashboard()
    time.sleep(2)
    
