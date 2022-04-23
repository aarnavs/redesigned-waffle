import urllib.request
import urllib.parse
import urllib.error
import json

url = 'https://py4e-data.dr-chuck.net/comments_1501408.json'

fx = urllib.request.urlopen(url).read().decode('utf-8')
js = json.loads(fx)
sum = 0
for item in js['comments']:
    sum += int(item['count'])


print('Sum: ', sum)
