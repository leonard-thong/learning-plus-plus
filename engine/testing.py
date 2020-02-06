import re
from selenium import webdriver

chrome = webdriver.Chrome("C:/Programming/Python/Selenium/chromedriver.exe")
chrome.get("https://www.oxfordreference.com/view/10.1093/acref/9780199688975.001.0001/acref-9780199688975")

l = []

for num in range(327):
    string = "https://www.oxfordreference.com/oso/viewbook.bookentries.pagedlist.gridpager/" + str(
        num) + "?btog=chap&hide=true&page=2&pageSize=20&skipEditions=true&sort=titlesort&source=%2F10.1093%2Facref%2F9780199688975.001.0001%2Facref-9780199688975&t:ac=10.1093$002facref$002f9780199688975.001.0001$002facref-9780199688975"

    chrome.close()
    chrome.get(string)
    s = chrome.page_source

    se = re.findall(r'<a href=\"/view/10.*\">(.+)</a>', s)
    for x in se:
        l.append(x)
