handler = open('textFile.txt','r')

import re
pattern = '[0-9]+'

data = re.findall(pattern, handler.read())

total = 0

for entry in data:
    intEntry = int(entry)
    total += intEntry

print(total)