import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET

url = 'https://py4e-data.dr-chuck.net/comments_1501407.xml'
print("Retrieving " + url)

xml = urllib.request.urlopen(url).read()
print("Retrieved: " + str(len(xml)) + " characters")

tree = ET.fromstring(xml)

counts =  tree.findall('.//count')
print("Count: " + str(len(counts)))

sum = 0

for count in counts:
    sum += int(count.text)

print("Sum:" + str(sum))
