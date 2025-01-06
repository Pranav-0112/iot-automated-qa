import psutil

def monitor_system():
    # Check CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

    # Check Memory Usage
    memory_info = psutil.virtual_memory()
    print(f"Memory Usage: {memory_info.percent}%")

    # Example: If CPU usage exceeds 85%, alert
    if cpu_usage > 85:
        print("Warning: High CPU usage detected!")

    # Example: If memory usage exceeds 90%, alert
    if memory_info.percent > 90:
        print("Warning: High memory usage detected!")

monitor_system()