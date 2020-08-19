# Test tasks
## Task 1
To run the script you need Python version >= 3.6 installed. To run the script execute `python random_numbers.py` in the terminal or use any other command for python which you have for Python version >= 3.6.

## Task 2
Since it's the only server which is used for SSL offloading and proxies it would be great to have resources utilization metrics:
- CPU usage
- RAM usage
- disk usage

Especially we are interested in CPU because it's used for encryption/decryption. But high usage of other listed resources also can lead to different
problems with system's work that's why there might be alarms for their usage. For monitoring opensource version of ELK stack can be used from Amazon
or Datadog, for example, if we talk about not open source. These metrics are usually standard for monitoring tools and should be easily configurable.

Then network metrics are essential:
- latency
- active connections
- bytes received
- bytes send

ELK stack can also be used here. Latency metric can be challengeable because we need to track responses and requests from different sources and
analyze it.

Also encryption/decryption time can be monitored as a part of latency.

Finally, it's important to check the expiration date for SSL certificate. This can be done with the script in the cron on the separate machine which
sends emails when the expiration date is close, for example.

Logs should be stored not on the server which we monitor so they won't be lost when the machine is broken.  
