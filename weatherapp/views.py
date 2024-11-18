from django.shortcuts import render
import requests
import datetime
from django.contrib import messages

# Create your views here.

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Kigali'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=050e97fd3a0c5746dedaa17667c16eb7'
    PARAMS = {'units': 'metric'}
    
    try:
        data = requests.get(url, PARAMS).json()
        print(data)
        
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        
        day = datetime.date.today()
        
        return render(request, 'index.html', {
            'description': description,
            'icon': icon,
            'temp':temp,
            'day': day,
            'city':city,
            'exception_occured': False
        })
    except:
        exception_occured = True
        messages.error(request, 'Entered Data not available ....')
        day = datetime.date.today()
        
        return render(request, 'index.html', {
            'exception_occured': exception_occured,
            'day': day,
            'exception_occured': True
        })