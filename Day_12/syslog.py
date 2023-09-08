import psutil
import time
import datetime

def monitor_system_processes(monitoring_interval, memory_threshold):
    while True:
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            logical_cpus = psutil.cpu_count(logical=True)
            used_memory = psutil.virtual_memory().percent
            used_disk_space = psutil.disk_usage('/').percent
            current_host_ip = psutil.net_if_addrs()['eth0'][0].address  # Update 'eth0' to your network interface

            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            log_line = f"{current_time}, {cpu_usage}, {logical_cpus}, {used_memory}, {used_disk_space}, {current_host_ip}\n"

            log_file_name = f"{current_time.split()[0]}-pub.log"

            with open(log_file_name, 'a') as log_file:
                log_file.write(log_line)

            if used_memory > memory_threshold:
                notification_log_file_name = f"{current_time.split()[0]}-notification.log"
                with open(notification_log_file_name, 'w') as notification_file:
                    notification_file.write("Low memory: System is running out of memory.")


            time.sleep(monitoring_interval)

        except KeyboardInterrupt:
            break

    print("Monitoring stopped.")


monitoring_interval = int(input("Enter monitoring interval in seconds: "))
memory_threshold = int(input("Enter memory threshold percentage: "))

monitor_system_processes(monitoring_interval, memory_threshold)
