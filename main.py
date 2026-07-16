import psutil 
print("Hello, World")

cpu_usage = psutil.cpu_percent(interval=1)
print("Current CPU usage:", cpu_usage, "%")

