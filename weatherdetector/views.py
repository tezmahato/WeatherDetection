from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def home(request):
    if request.method=='POST':
        city=request.POST['city']
        lon=urllib.request.urlopen('https://api.openweathermap.org/geo/1.0/direct?q='+city+'&limit=1&appid=de6edd293e76f879382a8bf09ebf3e97')
        json_data=json.load(lon)
        joson= json_data[0]
        prety_data= json.dumps(joson,indent=5)
        long=joson['lon']
        lat=joson['lat']

        res=urllib.request.urlopen(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&appid=de6edd293e76f879382a8bf09ebf3e97')    
        json_data=json.load(res)
        print(json_data)
        print(type(json_data))
        data={
            "city": city,
            "weather": json_data["weather"][0],
            "temperature": json_data["main"]["temp"],
            "lon":json_data["coord"]["lon"],
            "pressure": json_data["main"]["pressure"],
            "humidity": json_data["main"]["humidity"]
        }

        print(data["lon"])
    else:
        data={}

    return render(request,'index.html',data)