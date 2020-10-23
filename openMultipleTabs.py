## Script Goal -> Open Multiple Tabs

## Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

## Set up the driver
driverDashboard = webdriver.Firefox()

print('Launching 1st Set')
## Use this to open up my Dashboard
dashboardLinks = ['https://www.yahoo.com', 'https://www.cnn.com']

for link in dashboardLinks:
    driverDashboard.maximize_window()
    control_string = "window.open('{0}')".format(link)
    driverDashboard.execute_script(control_string)


## Use this to open up Ecom
## Setup eCom driver
driverEcom = webdriver.Firefox()
print('Launching 2nd Set')
eComLinks = ['https://www.trekbikes.com/us/en_US', 'https://www.pinkbike.com']

for link in eComLinks:
    driverEcom.maximize_window()
    control_string = "window.open('{0}')".format(link)
    driverEcom.execute_script(control_string)


# TODO Now add a chrome bit


# Run a ping and open an app
print('Pinging')
import os
os.system("start cmd /k ping 8.8.8.8")


# # Launch explorer and navigate to a folder
print('Opening SSH folder')
import subprocess
subprocess.Popen(r'explorer /select,"C:\Users\jpkee\.ssh"')


import subprocess
# Replace this with ADB 
# subprocess.call(['C:\\Program Files\\Firefox Developer Edition\\firefox.exe'])

# run my network checks
import os
print ('Starting Pings!')
ip_list = ['8.8.8.8', '192.168.1.1']
for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 4" in response:
        print(f"{ip} Ping Successful")
    else:
        print(f"{ip} Ping Unsuccessful")


# Print a Finished Message
print('\nAll Done')

