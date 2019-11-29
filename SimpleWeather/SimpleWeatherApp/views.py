import requests
from django.shortcuts import render
from .models import Location
from .forms import LocationForm


def Home(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=APIKEY'

    if request.method == 'POST':
        form = LocationForm(request.POST)
        form.save()

    form = LocationForm()

    locations = Location.objects.all()

    weather_data = []
    if locations and len(locations) > 0:
        for location in locations:
            r = requests.get(url.format(location)).json()

            location_weather = {
                'location': location.name,
                'temperature': r['main']['temp'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
            }

            weather_data.append(location_weather)

        context = {'weather_data': weather_data, 'form': form}
        return render(request, 'weather.html', context)
    else:
        return render(request, '404.html')
