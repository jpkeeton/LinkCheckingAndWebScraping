# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")

# We're starting the test
print("Starting test\n")

# Set up the driver
driver = webdriver.Firefox()

# Grab the url
driver.get("http://www.python.org")

# title = driver.title

# Make an assertion
assert "Python" in driver.title


# print('Title is: ' + title)


# Find an element
elem = driver.find_element_by_name("q")



# Enter some text
elem.send_keys("pycon")
time.sleep(3)
# Hit enter
elem.send_keys(Keys.RETURN)

# Make sure we found something
assert "No results found." not in driver.page_source

# Sleep example
# time.sleep(10)

# TODO make it headless with this bit
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.add_argument("--headless")



# Close the broswer
driver.close()

# Inform that we are done
print("\nEnding test & closing browser")
