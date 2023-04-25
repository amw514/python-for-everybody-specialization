import xml.etree.ElementTree as ET
data = '''<person>
<name>Chuck</name>
<phone type="intl">123-456-7890</phone>
<email>bob@example.com</email>
</person>'''


tree = ET.fromstring(data)

print("Name:",tree.find('name').text)
