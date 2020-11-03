# Imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time 

# <<
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.add_argument("--headless")
# >>

# <><>
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# options = Options()
# options.headless = True
# driver = webdriver.Chrome(options=options, executable_path=r'C:\path\to\chromedriver.exe')
# driver.get("http://google.com/")
# print ("Headless Chrome Initialized")
# driver.quit()

# <>>

executable_path={'executable_path':r'C:\Users\jpkee\Downloads\chromedriver_win32\chromedriver.exe'}
# Create a browser instance
browser = Browser('chrome', **executable_path, headless=True)



# We're starting the test
print("Starting test\n")

# Set up the driver for Firefox
# driver = webdriver.Firefox()



# Grab the url
browser.get("http://www.python.org")



# title = driver.title

# Make an assertion
assert "Python" in driver.title

# Print out the title
print('Title is: ' + title)


# Find an element, in this case the search box
elem = driver.find_element_by_name("q")



# Enter some text into search box
elem.send_keys("pycon")
time.sleep(3)
# Hit enter
elem.send_keys(Keys.RETURN)

# Make sure we found something
assert "No results found." not in driver.page_source



# TODO make it headless with this bit
# from selenium.webdriver.chrome.options import Options
# options = Options()
# options.add_argument("--headless")



# Close the broswer
# driver.close()

# Quite the browser
driver.quit()

# driver.quit() = exit the browser, end the session, tabs, pop-ups etc. 
# driver.close() = only the window that has focus is closed.

# Inform that we are done
print("\nEnding test & closing browser")
