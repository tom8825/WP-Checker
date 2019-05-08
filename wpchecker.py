from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = input("What URL would you like to check?")
html = urlopen(url)
bsObj = BeautifulSoup(html.read())
foundCount = 0

for link in bsObj.find_all('link'):
    
    if ("wp-content" in link.get('href')): 
        m = re.search('\/wp-content\/themes\/([\w]{1,})\/.*', link.get('href'))
        if m:
            found = m.group(1)
        else:
            print("This is not a WordPress site.")
            break
        print("This website uses the theme: " + found)
        foundCount += 1
        break
     
    