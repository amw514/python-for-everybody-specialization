import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

link = input('Enter Location: ')

html = urllib.request.urlopen(link).read().decode()
print("Retrieving", link)
print("Retrieved",len(html),"characters")

#Data Calculation
counts= 0
sum = 0

data = ET.fromstring(html)

tags = data.findall("comments/comment")

print(tags)
for item in tags:
    counts+=1
    sum += int(item.find('count').text)
    
print("Counts", counts)
print("Sum", sum)
    