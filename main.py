import psutil 

text = "SYSTEM MONITOR DASHBOARD"
print("="*50)
print(f"{text: ^50}") # Center-aligned with `-`
print("="*50)
print()



cpu_usage = psutil.cpu_percent(interval=1)
print(f"{'CPU Usage:':<25}{cpu_usage}%")

memory_usage = psutil.virtual_memory().percent
print(f"{'Memory Usage:':<25}{memory_usage}%")

disk_space_taken = psutil.disk_usage('/').percent
print(f"{'Disk Usage:':<25}{disk_space_taken}%")   