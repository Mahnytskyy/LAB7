import requests
from bs4 import BeautifulSoup
import pylab

r = requests.get("https://osvita.ua/school/literature/f/65158/list-1.html")
page = BeautifulSoup(r.text, 'html.parser')
print(r.status_code)
ryadok1=page.head.title.text
ryadok2=page.body.text
names=["Звичайні","Питальні","Пкличні", "Три крапки"]
frequency=[0,0,0,0]
frequency[0]=ryadok2.count('.')
frequency[1]=ryadok2.count('?')
frequency[2]=ryadok2.count('!')
frequency[3]=ryadok2.count('...')
xdata=names
ydata=frequency
pylab.bar (xdata, ydata)
pylab.show()