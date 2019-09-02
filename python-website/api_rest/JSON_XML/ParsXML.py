import urllib.request
import xml.etree.ElementTree as ET

url = 'https://www.w3schools.com/xml/cd_catalog.xml'

data = urllib.request.urlopen(url).read() ##Con read leo los datos

tree = ET.fromstring(data.decode())

lst = tree.findall('CD')

print("Número de CDs", len(lst))

for item in lst:
    print('\r')
    print('Title', item.find('TITLE').text)