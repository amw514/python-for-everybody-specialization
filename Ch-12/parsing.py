import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup

url = input("Enter a URL: ")

html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')

for tag in tags:
    print(tag.get('href',None))