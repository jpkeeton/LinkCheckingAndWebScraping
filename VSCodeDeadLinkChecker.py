# Set Imports
import csv
import re
import time
import os
from datetime import datetime
import urllib.request
import requests
# import httplib2
from bs4 import BeautifulSoup, SoupStrainer
# from selenium import webdriver
from splinter import Browser


# TODO Set headers
# https://hackersandslackers.com/scraping-urls-with-beautifulsoup/


# Starting timer
startTime = datetime.now()

# User enters a web site address.

site_to_visit = input("Please enter an address: ") 

# Driver location
executable_path={'executable_path':r'C:\Users\jpkee\Downloads\chromedriver_win32\chromedriver.exe'}
# Create a Chrombrowser instance, in this case make it headless
browser = Browser('chrome', **executable_path, headless=True)

# Add 'https://' if needed
if not site_to_visit.startswith("http"):
    site_to_visit = "https://" + site_to_visit

# Stick the user input into the visit function
print('Hold please, we\'re checking....' + site_to_visit)


# checking to see if I can get a 200 here
request = requests.get(site_to_visit)
if request.status_code == 200:
    print('looks good, lets continue')   
else:
    print('site is busted')


# launch browser
browser.visit(site_to_visit)

# Just tell user of the links we found
print('Here are the links I found: ')

# Create a parser
parser = 'html.parser' 
    # lxml or html5lib can also be used
    # resp here is creating a urllib request and I'm sticking the site to visit in as parameter
resp = urllib.request.urlopen(site_to_visit)
soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))





# second version
for link in soup.find_all('a', href=True):
    print(link['href'])
        # comment this out
    # if link['href'].startswith('http'):
        # so it's in here, i don't need to get code for all of these, it's also giving me 403 problems
        # comment this out
        # print(urllib.request.urlopen(link['href']).getcode())
        # so here we're finding #content, referring to anchor/tag
    # just print the hrefs!

print('Number of links: ' + str(len(site_to_visit)))


# TODO how to find all image tags?
# soup.find_all



# maybe try using a list comprehension for this? in the below format
# even_squaresFormatted = [x * x 
#                 for x in range(10) 
#                 if x % 2 == 0]

# add a timer!
print('This test took: ' + (str(datetime.now() - startTime)) + ' Seconds')

# TODO Figure out why FQDNs are giving me a 200, only the primary domain needs to be checked 

# End test and quit browser    
print('Ending test')
browser.quit()