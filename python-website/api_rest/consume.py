import requests
import os 
api_key= os.getenv("open_weather_key")

parameter = {"mode":"json","units":"metric","APPID":api_key}
print("Ciudad a buscar")
c = input()
parameter["q"] = c
#parameter = {"q":c,"mode":"json","units":"metric","APPID":api_key} tambien se puede asi

try:
    r = requests.get("http://api.openweathermap.org/data/2.5/weather",params=parameter)
    
    if r.status_code==200:
        print("*Searching for*",c)
        datos = r.json()
        print("Temperature :",datos["main"]["temp"],"ºC")
    else:
        print("No data available", r.status_code)
except:
    print("Something went wrong")