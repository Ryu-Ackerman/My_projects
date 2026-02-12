import requests
import sys

def forecast():
    c = input('Enter the city/country name: ').lower()
    api_1 = f'https://geocoding-api.open-meteo.com/v1/search?name={c}'


    try:
        r = requests.get(api_1)
        j = r.json()
        if not j['results']:
            sys.exit("City not found. Check the spelling please!")
        for index, i in enumerate(j['results']):
            print(f"{index+1}){i['name']}, {i['country']}")


        while True:
            try:
                user = input("Enter the number of the intended city/country: ").lower()
                if int(user) < 1 or int(user) > len(j['results']):
                    print('Input out of range!')
                    continue
                break
            except ValueError:
                if user == "quit":
                    sys.exit('You successfully quit the program!')
                else:
                    print("Invalid input!")
                    continue


        longitude = j['results'][int(user) - 1]['longitude']
        latitude = j['results'][int(user) -1]['latitude']
        api3 = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,precipitation_probability&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone=auto"


        r2 = requests.get(api3)
        j2 = r2.json()
        print(j2['daily']['time'])
    except (requests.exceptions.RequestException):
        sys.exit('Connection error!')

forecast()