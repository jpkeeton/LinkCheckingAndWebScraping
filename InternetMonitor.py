
# Monitor your internet
# https://pythonprogramming.org/monitor-your-internet-with-python/


# check that matplotlib is installed
# install speedtest cli


# import speedtest

# s = speedtest.Speedtest()
# while True:
#     print(s.download(), s.upload())

# print(s)


# import speedtest
# import datetime
# import time
# s = speedtest.Speedtest()

# while True:
#     time_now = datetime.datetime.now().strftime("%H:%M:%S")
#     downspeed = round((round(s.download()) / 1048576), 2)
#     upspeed = round((round(s.upload()) / 1048576), 2)
#     print(f"time: {time_now}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")
#     # 60 seconds sleep
#     time.sleep(5)




import speedtest
import datetime
import csv
import time

s = speedtest.Speedtest()

with open('test.csv', mode='w') as speedcsv:
    csv_writer = csv.DictWriter(speedcsv, fieldnames=['time', 'downspeed', 'upspeed'])
    csv_writer.writeheader()
    while True:
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        downspeed = round((round(s.download()) / 1048576), 2)
        upspeed = round((round(s.upload()) / 1048576), 2)
        csv_writer.writerow({
            'time': time_now,
            'downspeed': downspeed,
            "upspeed": upspeed
        })
        # 60 seconds sleep
        time.sleep(60)