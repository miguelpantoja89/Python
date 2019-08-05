from bs4 import BeautifulSoup
import requests
import pandas as pd 


url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion'

page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')

#Find Football Teams

tm = soup.find_all('span',class_= 'nombre-equipo')

teams = list()

cont = 0
for e in tm:
    if cont < 20:
        teams.append(e.text)
    else:
        break
    cont +=1

# Points 

pt= soup.find_all('td',class_='destacado')

points = list()

count = 0 #First 20 items
for i in pt:
    if count < 20:
        points.append(i.text)
    else:
        break
    count +=1

# Create the dataframe

dataframe = pd.DataFrame({'Name': teams,'Points': points}, index= list(range(1,21)))

dataframe.to_csv('results.csv', index=False)

