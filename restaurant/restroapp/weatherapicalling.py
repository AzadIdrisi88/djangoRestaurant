import requests
from.models import apimodel
def getWeather(city):
    appid="185a5b60b5b86a369f84a06359abb723"
    url="https://api.openweathermap.org/data/2.5/weather?q={1}&appid={0}&units=metric".format(appid,city)
    # url = "https://api.openweathermap.org/data/2.5/forecast?lat=25.3333&lon=83&appid=4a1f8a61b74546825af1e0be106e797b&units=metric"
    response=requests.get(url)
    return response.text
   

cities="Delhi,Lucknow,Varanasi,Jaipur,jaunpur,Mumbai"
cities=cities.split(",")
for city in cities:
    data=getWeather(city)
    jsondata=data
    print(city,"\n",data,",",len(data),"\n")
    print(len(data),"\n")
    ob=apimodel()
    ob.city=city
    ob.jsondata=jsondata
    ob.save()