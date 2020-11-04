# https://pythonbasics.org/selenium-firefox-headless/
# headless example

import os
from datetime import datetime
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

startTime = datetime.now()
# Set options
options = Options()
options.headless = True

# Trying to get the browser launches
print('Starting Headless Test')

try:
    browser = webdriver.Firefox(options=options)
    browser.get('https://www.cnn.com')

# TODO: check to see if the site is alive and if so, proceed
    request = requests.get(browser)
    if browser.status_code != 200:
        print('looks like a bad link, try again')
    else:
        print('that is alive, let us continue')

# commenting this out for a min
# print(browser.page_source)
# just print the page title instead of the source
    # print('The browser title is: ' + browser.title)

    # so maybe run this twice headless and headed and then commpare the times, do a caculation
        # print out something like 'headed took x time, headless took y time, so total difference is z'

finally:
    try:
        print("Quitting Browser")        
        browser.quit()
    except:
        pass
# Timer bit
# print('This test took: ' + (str(datetime.now() - startTime)) + ' Seconds')
