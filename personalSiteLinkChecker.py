# Testing my personal website:
# Next, the instance of Chrome WebDriver is created.
import csv
import re
import time
import os
from datetime import datetime
import urllib.request
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
# import httplib2
from bs4 import BeautifulSoup, SoupStrainer
# from selenium import webdriver
from splinter import Browser
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--window-size=1920x1080")
# pointing to the specific driver version here
driver = webdriver.Chrome(executable_path=r'C:\Users\jpkee\Downloads\chromedriver_win32\chromedriver.exe')


# executable_path={'executable_path':r'C:\Users\jpkee\Downloads\chromedriver_win32\chromedriver.exe'}
# browser = Browser('chrome', **executable_path, headless=True)




# the driver.get method will navigate to a page given by the URL
# Webdriver will wait unti lthe page has fully loaded, aka the 'onload' event has fired
startTime = datetime.now()
driver.get('https://jeremypk.net')

print("Kickin' off the test!")
# assert "jeremypk" in driver.title



# parser = 'html.parser' 
# resp = urllib.request.urlopen(driver)
# soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))
# for link in soup.find_all('a', href=True):
#     print(link['href'])



# Find all the hrefs on my site
# blogLinkCheck = 'https://jeremypk.net/blog-feed/'
# element = driver.find_element_by_link_text(blogLinkCheck)
# links = driver.find_elements_by_xpath("//a[@href]")
# for link in links:
#     print(link.get_attribute("href"))
    
# assert blog feed is there
# https://jeremypk.net/blog-feed/
# blogFeed = driver.find_elements_by_xpath("https://jeremypk.net/blog-feed/")

 
# src = driver.page_source
# blogFeed = re.search(r'Blog Feed', src)
# self.assertNotEqual(text_found, None)


# Here I'm clicking all the links on my Wordpress site
blogFeed=driver.find_element_by_link_text("Blog Feed")
blogFeed.click()
# time.sleep(1)
driver.back()

print('clicking software testing')
testing=driver.find_element_by_link_text("Software Testing/QA")
testing.click()
# time.sleep(1)
driver.back()


trainings=driver.find_element_by_link_text("Trainings & Certificates")
trainings.click()
# time.sleep(1)
driver.back()


dataViz=driver.find_element_by_link_text("Data Visualization Gallery")
dataViz.click()
# time.sleep(1)
driver.back()

bookshelf=driver.find_element_by_link_text("Bookshelf")
bookshelf.click()
# time.sleep(1)
driver.back()


about=driver.find_element_by_link_text("About Me")
about.click()
# time.sleep(1)
driver.back()
# time.sleep(1)



# elem = driver.find_element_by_name("q")
# # would be cool to have an if presen here probably
# if driver.find_elements_by_name('q'):
#     print("Found the search box")
# else:
#     print("I'm not finding the search box")
#     driver.close()
# Find this link
# https://jeremypk.net/blog-feed
#     https://stackoverflow.com/questions/33155454/how-to-find-an-element-by-href-value-using-selenium-python/33155512
    # or this approach? 
  # https://stackoverflow.com/questions/45695874/check-if-element-exists-python-selenium            



title = driver.title
print('Title is: ' + title)

# assert "No results found." not in driver.page_source
print('Quitting Browser')
driver.quit()
print('This test took: ' + (str(datetime.now() - startTime)) + ' Seconds')
