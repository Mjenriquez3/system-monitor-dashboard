import psutil 
print("Hello, World")

cpu_usage = psutil.cpu_percent(interval=1)
print("Current CPU usage:", cpu_usage, "%")

memory_usage = psutil.virtual_memory().percent
print("Current Memory usage:", memory_usage, "%")

disk_spaceTaken = psutil.disk_usage('/').percent
print("Current Disk usage:", disk_spaceTaken, "%")