# # This will grab HTML
# ## Grab the html

# # from urllib.request import urlopen
# # findRobots = urlopen("http://www.google.com/").read()
# # print(findRobots)


# # Another example here:
# # Source: https://github.com/realpython/python-scripts/blob/master/scripts/02_find_all_links.py
# import requests
# import re
# # get url
# url = input('Enter a URL (include `http://`): ')
# # connect to the url
# website = requests.get(url)
# # read html
# html = website.text
# # use re.findall to grab all the links
# links = re.findall('"((http|ftp)s?://.*?)"', html)
# # output links
# for link in links:
#     print(link[0])


# # Grabs links also
# import urllib.request
# from bs4 import BeautifulSoup, SoupStrainer
# import re

# site_to_visit = 'https://www.python.org'
# html_page = urllib.request.urlopen(site_to_visit).read()
# soup = BeautifulSoup(html_page)
# for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
#     print(link.get('href'))


# # Extract all images
# from bs4 import BeautifulSoup
# import urllib2
# import re

# html_page = urllib2.urlopen("jeremypk.net")
# soup = BeautifulSoup(html_page)
# images = []
# for img in soup.findAll('img'):
#     images.append(img.get('src'))

# print(images)


# # Check status of a site_to_visit

# import urllib.request
# print(urllib.request.urlopen("http://www.stackoverflow.com").getcode())

# # or you can use this style with requests
# import requests

# def url_ok(url):
#     r = requests.head("http://www.stackoverflow.com")
#     return r.status_code == 200


# # so stick this into my for loop
# import urllib.request
# url = ("https://www.google.com")

# status_code = urllib.request.urlopen(url).getcode()
# website_is_up = status_code == 200

# # print(website_is_up)


# Another status checker example:
# import urllib.request as urllib

# req = urllib.Request('http://www.python.org/fish.html')
# try:
#     resp = urllib.urlopen(req)
# except urllib.HTTPError as e:
#     if e.code == 404:
#         print('first if bit')
#     else:
#         print('this is the else bit')
# except urllib.URLError as e:
#     # Not an HTTP-specific error (e.g. connection refused)
#     print("this is the exception")
# else:
#     print('another else bit')
#     body = resp.read()


# import urllib.request
# print('about to this this')
# urllib.request.urlopen('http://216.58.192.142',timeout=0)



# for i in range(0, len(table)):
#         var = table.iloc[i]
#         url = 'http://example.request.com/var/'
#         response = requests.get(url)
#         while response.status_code != 200:
#             response = requests.get(url)     
#         data = response.json()


# how to stop the program after certain amount of time
# import time
# start = time.time()
# PERIOD_OF_TIME = 300 # 5min
# while True :
#     # ... do something
#     if time.time() > start + PERIOD_OF_TIME : break




# putting links into a csv
#     with open("Found Links",'w') as csvfile:
#         write = csv.writer(csvfile, delimiter = ' ')
#         write.writerows(link)

# can i stick these into an excel sheet
# https://stackoverflow.com/questions/59509411/python-selenium-csv-how-to-open-links-from-list-in-csv-file-loop-code-ap

#  with open('Found Links', 'w', newline='') as csvfile:
#     write = csv.writer(csvfile)
#     write.writerows(link)




# maybe try using a list comprehension for this? in the below format
# even_squaresFormatted = [x * x 
#                 for x in range(10) 
#                 if x % 2 == 0]




# TODO: check each link status, using getcode
# import urllib.request
# print(urllib.request.urlopen("http://www.jeremypk.net").getcode())
# # print(urllib.request.urlopen(link).getcode())



# import requests

# URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
# page = requests.get(URL)
# print(page)


import requests
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)
print('the link  gave me back: ' + str(page))



# Window sizings
    # driverDashboard.set_window_size(180000, 1400)
    # driverDashboard.maximize_window()


# this was the old linkchecker bit I was using, checking every link for get code which is not needed
    # Looping thru all the anchor hrefs, first version
    # for link in soup.find_all('a', href=True):
    #     print(link['href'])
    #     if link['href'].startswith('http'):
    #         # so it's in here, i don't need to get code for all of these, it's also giving me 403 problems
    #         print(urllib.request.urlopen(link['href']).getcode())
    #         # so here we're finding #content, referring to anchor/tag




# code for checking execution duration
import os
from datetime import datetime

print ('Starting Pings!')
startTime = datetime.now()
ip_list = ['8.8.8.8', '192.168.1.1']
for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 4" in response:
        print(f"{ip} Ping Successful")
    else:
        print(f"{ip} Ping Unsuccessful")
        
# So how long did this take?
print('This test took: ' + (str(datetime.now() - startTime)) + ' Seconds')
# print(datetime.now() - startTime)
# or more verbosely