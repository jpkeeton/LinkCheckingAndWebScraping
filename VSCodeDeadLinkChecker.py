# Set Imports
import csv
import re
import time
import urllib.request
import requests
import httplib2
from bs4 import BeautifulSoup, SoupStrainer
from selenium import webdriver
from splinter import Browser

# User enters a web site address.
site_to_visit = input("Please enter your address: ") 

# Driver location
executable_path={'executable_path':r'C:\Users\jpkee\Downloads\chromedriver_win32\chromedriver.exe'}
# Create a browser instance
browser = Browser('chrome', **executable_path, headless=True)

# Add 'https://' to the front if the link doesn't start with 'http'
if not site_to_visit.startswith("http"):
    site_to_visit = "https://" + site_to_visit

# stick the user input into the visit function
print('Hold please, we\'re checking....' + site_to_visit)
browser.visit(site_to_visit)

# checking to see if I can get a 200 here
request = requests.get(site_to_visit)
if request.status_code != 200:
    print('looks like a bad link, try again')   
else:
    print('that is alive, let us continue') 


# Just tell user of the links we found
print('Here are the links I found: ')

# create a parser
parser = 'html.parser' 
# # lxml or html5lib can also be used
# resp here is creating a urllib request and I'm sticking the stite to visit in as parameter
resp = urllib.request.urlopen(site_to_visit)
soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))

# Looping thru all the anchor hrefs
for link in soup.find_all('a', href=True):
    print(link['href'])
    # print(urllib.request.urlopen(link).getcode())





    # grabbing the status codes here:
    # print(urllib.request.urlopen("http://www.jeremypk.net").getcode())
    # print(urllib.request.urlopen(link).getcode())

#     with open("Found Links",'w') as csvfile:
#         write = csv.writer(csvfile, delimiter = ' ')
#         write.writerows(link)

# can i stick these into an excel sheet
# https://stackoverflow.com/questions/59509411/python-selenium-csv-how-to-open-links-from-list-in-csv-file-loop-code-ap

#  with open('Found Links', 'w', newline='') as csvfile:
#     write = csv.writer(csvfile)
#     write.writerows(link)


# TODO: check each link status
# print(urllib.request.urlopen("http://www.jeremypk.net").getcode())
# so checking each link will need the .getcode bit





# End test and quit browser    
print('Ending test')
browser.quit()
