import psutil
import subprocess
import requests
import json

# Function to check CPU usage
def check_cpu():
    cpu_usage = psutil.cpu_percent()
    if cpu_usage > 80:
        message = "CPU usage is high: " + str(cpu_usage) + "%"
        send_slack_notification(message)

# Function to check RAM usage
def check_ram():
    ram_usage = psutil.virtual_memory().percent
    if ram_usage > 80:
        message = "RAM usage is high: " + str(ram_usage) + "%"
        send_slack_notification(message)

# Function to check disk usage
def check_disk():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > 80:
        message = "Disk usage is high: " + str(disk_usage) + "%"
        send_slack_notification(message)

# Function to check logs for errors
def check_logs():
    command = "grep -i error /var/log/syslog"
    output = subprocess.check_output(command, shell=True)
    if output:
        message = "Errors found in logs: " + str(output)
        send_slack_notification(message)

# Function to send Slack notification
def send_slack_notification(message):
    slack_url = "https://hooks.slack.com/services/XXXXXXXXX/XXXXXXXXX/XXXXXXXXXXXXXXXXXXXXXXXX"
    slack_data = {'text': message}
    response = requests.post(slack_url, data=json.dumps(slack_data), headers={'Content-Type': 'application/json'})
    if response.status_code != 200:
        raise ValueError('Slack notification failed: ' + response.text)

# Main function to check resources and logs
def main():
    check_cpu()
    check_ram()
    check_disk()
    check_logs()

if __name__ == '__main__':
    main()