# import requests
# import lxml.html

# # This code is from: https://data-lessons.github.io/library-webscraping-DEPRECATED/04-lxml/

# # response = requests.get('http://www.un.org/en/sc/documents/resolutions/2016.shtml')
# response = requests.get('http://www.cnn.com')
# tree = lxml.html.fromstring(response.text)
# title_elem = tree.xpath('//title')[0]
# # title_elem = tree.cssselect('title')[0]  # equivalent to previous XPath
# print("title tag:", title_elem.tag)
# print("title text:", title_elem.text_content())
# print("title html:", lxml.html.tostring(title_elem))
# print("title tag:", title_elem.tag)
# print("title's parent's tag:", title_elem.getparent().tag)

# # file = open(file_name, 'wb')
# # print('Collecting the links...')
# # for link in links:
# #     href = link.get('href') + '\n'
# #     file.write(href.encode())
# # file.close()
# # print('Saved to %s' % file_name)





import selenium.webdriver


executable_path={'executable_path':r'C:\Users\jpkee\Downloads\chromedriver_win32\chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=True)


driver = selenium.webdriver.Chrome() # Firefox()

driver.get('https://travel.padi.com/s/liveaboards/caribbean/')

all_cards = driver.find_elements_by_xpath('//div[@class="boat search-page-item-card "]')

for card in all_cards:
    title = card.find_element_by_xpath('.//a[@class="shop-title"]/span')
    desc  = card.find_element_by_xpath('.//p[@class="shop-desc-text"]')
    price = card.find_element_by_xpath('.//p[@class="cur-price"]/strong/span')

    print('title:', title.text)
    print('desc:',  desc.text)
    print('price:', price.text)

    all_dates = card.find_elements_by_css_selector('.cell.date')

    for date in all_dates:
        day, month = date.find_elements_by_tag_name('span')
        print('date:', day.text, month.text)

    print('---')