import requests
from datetime import datetime

with open('apikey.txt') as file:
    key = file.readline()

location = input('Enter Location: ')

print()
print(key)
print('\n\n')

# making api call
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

link = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={key}'

api_link = requests.get(link)
api_data = api_link.json()

if api_data['cod'] == '404':
    print('Error in connectig to API')
    for data in api_data:
        print(data + ': ' + api_data[data])
        print()
else:
    print(api_data['cod'])
    print()
    date = 'Date: ' + str(datetime.now().strftime("%d %b %Y"))
    time = 'Time: ' + str(datetime.now().strftime("%1:%M:%S %p"))
    city = 'City: ' + str(api_data['name'])
    current_temp = 'Current temperature: ' + str(round(api_data['main']['temp'] - 273.15, 2)) + ' Degree Celsius'
    feels_like = 'Feels like: ' + str(round(api_data['main']['feels_like'] - 273.15, 2)) + ' Degree Celsius'
    humidity = 'Humidity: ' + str(api_data['main']['humidity']) + '%'
    min_temp = 'Minimum temerature: ' + str(round(api_data['main']['temp_min'] - 273.15, 2)) + ' Degree Celsius'
    max_temp = 'Maximum temperature: ' + str(round(api_data['main']['temp_max'] - 273.15, 2)) + ' Degree Celsius'
    visibility = 'Visibility: ' + str(api_data['visibility']/1000) + ' Km'
    clouds = 'Cloudiness: ' + str(api_data['clouds']['all']) + '%'

    weather_data = [city, date, time, current_temp, feels_like, humidity, visibility, clouds,]

    for data in weather_data:
        print(data)
        print()

print('*' * 50)



