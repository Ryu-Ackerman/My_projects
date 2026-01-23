import requests
import sys
import collections
import csv



class Collect_data():
    def __init__(self, city, temp, windspeed, date):
        self.city = city
        self.temp = temp
        self.windspeed = windspeed
        self.date = date


    def turn_dict(self):
        return {
            'city': self.city,
            'temperature': self.temp,
            'windspeed': self.windspeed,
            'date-time': self.date
        }




def display_saved():
        with open('kregg.csv') as f:
            for i in f:
                print(i, end='')
        sys.exit()



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
        units = j2['daily']
        ind = range(1,8)
        maxt = units['temperature_2m_max']
        mint = units['temperature_2m_min']
        print('Highest|Lowest')
        for z,i,x in zip(ind,maxt, mint):
            print(f'{z}){i}|{x}')
    except (requests.exceptions.RequestException):
        sys.exit('Connection error!')

    
def average():
        while True:
            try:
                dys = input('Enter the number of days you wanna see the average of: ').lower()
                lines('krg.csv', int(dys))
                sys.exit()
            except ValueError:
                if dys != 'quit':
                    print('Invalid input')
                    continue
                else:
                    sys.exit()


                    
def get_country():
    c = " ".join(sys.argv[1:]).lower()
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
        api_2 = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true'
        r_2 = requests.get(api_2)
        j_2 = r_2.json()
        temp = j_2['current_weather']['temperature']
        w_S = j_2['current_weather']['windspeed']
        day = j_2['current_weather']['is_day']
        date = j_2['current_weather']['time']
        print(f"The temperature is {temp}°C")
        print(f"The windspeed is {w_S} km/h")
        if day == 1:
            print('Day time')
        else: 
            print('Night time')
        with open('krg.csv', 'a', newline='') as f:
            columns = ['city', 'temperature', 'windspeed' ,'date-time']
            writer = csv.DictWriter(f, fieldnames=columns)
            # writer.writeheader()
            form = Collect_data(c, temp, w_S, date)
            writer.writerow(form.turn_dict())
    except requests.exceptions.RequestException:
        print("Check your connection sir!")
    except(KeyError, ValueError):
        print('City/country not found check the spelling!')



def lines(directory, num_of_days):
    tem = []
    w__s = []
    with open(directory) as f:
        reader = csv.DictReader(f)
        for i in reader:
            temps = i['temperature']
            tem.append(float(temps))
            ws = i['windspeed']
            w__s.append(float(ws))
        avg_temp = sum(tem)/len(tem)    
        avg_ws = sum(w__s)/len(w__s)
        print(f'The average windspeed in the last {num_of_days} day(s) is {round(avg_temp, 1)} km/h')
        print(f'The average windspeed in the last {num_of_days} day(s) is {round(avg_ws, 1)} km/h') 



funcs = {
    'average': average,
    'saved': display_saved,
    'forecast': forecast,
    '<name of a country>':lambda:None,
    '-h': lambda: [print("*",k) for k in funcs.keys()],
}



def main():
    if len(sys.argv) < 2:
        sys.exit("Not enough arguments on the terminal!\n-h for for help")
    command = funcs.get(sys.argv[1])
    if command:
        command()
    else:
        get_country()



if __name__ == "__main__":
    main()