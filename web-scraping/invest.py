import sys
import urllib.request
from bs4 import BeautifulSoup
participaciones = 50 
url= 'http://www.morningstarfunds.ie/ie/funds/snapshot/snapshot.aspx?id=F00000PJME'
html= urllib.request.urlopen(url)
soup = BeautifulSoup(html)
tags = soup.find_all("td",class_="line text") # Extraigo las etiquetas 
valor = float(tags[0].contents[0].replace('EUR\xa0','')) # Me quedo únicamente con el valor numérico
total = participaciones * valor
print(total)