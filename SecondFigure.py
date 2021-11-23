import requests
from bs4 import BeautifulSoup
from array import *
import csv
import pylab

r = requests.get("https://www.reddit.com/")
page = BeautifulSoup(r.text, 'html.parser')
print(r.status_code)
ryadok1=page.head.title.text
ryadok2=page.body.text
letters_str='abcdefghijklmnopqrstuvwxyz'
letters=list(letters_str)
frequency=[]
L=len(letters)
for i in range(L):
    elem=letters[i]
    fr=ryadok2.count(elem)
    frequency.append(fr)
xdata=letters
ydata=frequency
pylab.bar(xdata, ydata)
pylab.show()    