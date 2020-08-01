from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter-')
html = urlopen(url,context = ctx).read()
s = BeautifulSoup(html,"html.parser")

sum = 0
c = 0
tags = s('span') #tag you want to search
for i in tags:
    c += 1
    sum = sum + int(i.contents[0])
print('count',c)
print('Sum',sum)
