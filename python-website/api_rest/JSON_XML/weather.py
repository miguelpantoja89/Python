import urllib.request
import json


url = "https://api.openaq.org/v1/cities"

url2 = "https://api.openaq.org/v1/latest"

country = input('Introduce la siglas del país (ejmplo ES para España ) \n')

consult = url + '?country=' + country

data = urllib.request.urlopen(consult).read().decode()

js = json.loads(data)

for i in range(25):
    city = js['results'][i]['city']
    print(city)


ciudad = input('Introduce una ciudad de la lista anterior\n')

consult2 = url2 + '?limit=1&city=' + ciudad

data2 = urllib.request.urlopen(consult2).read().decode()

js2 = json.loads(data2)

par = js2['results'][0]['measurements'][0]['parameter']
val = js2['results'][0]['measurements'][0]['value']
uni = js2['results'][0]['measurements'][0]['unit']

print('El valor de ', par, 'en', ciudad, 'es de', val, uni)