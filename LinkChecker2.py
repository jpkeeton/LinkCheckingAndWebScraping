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
    # lxml or html5lib can also be used
    # resp here is creating a urllib request and I'm sticking the stite to visit in as parameter
resp = urllib.request.urlopen(site_to_visit)
soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))

# Looping thru all the anchor hrefs
for link in soup.find_all('a', href=True):
    print(link['href'])
    print(urllib.request.urlopen(link).getcode())


# maybe try using a list comprehension for this? in the below format
# even_squaresFormatted = [x * x 
#                 for x in range(10) 
#                 if x % 2 == 0]



# TODO: check each link status, using getcode
import urllib.request
print(urllib.request.urlopen("http://www.jeremypk.net").getcode())
# print(urllib.request.urlopen(link).getcode())






# End test and quit browser    
print('Ending test')
browser.quit()
