# checkServerResourcesWithPython

Python code that checks the resources of CPU, RAM, and disk, and logs errors in the logs of a Linux server. It also sends a notification to Slack if something fails:

This code is using the `psutil` package to check the CPU, RAM, and disk usage. It is also using the `subprocess` module to check the logs for errors. If any of the resources exceed 80%, or if any errors are found in the logs, a Slack notification is sent using the `requests` module.
