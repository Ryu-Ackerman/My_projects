import requests
import sys
import collections

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


def total():
        nums = []
        med_temp = []
        med_wind = []
        with open('kregg.csv') as f:
            reader = f.read()
            for i in reader.split():
                try:
                    float(i)
                    nums.append(float(i))
                except ValueError:
                    pass
        for x in nums[0::2]:
            med_temp.append(float(x))
        for y in nums[1::2]:
            med_wind.append(float(y))
        avg1 = sum(med_temp)/len(med_temp)
        avg2 = sum(med_wind)/len(med_wind)
        print(f"The average temperature is {round(avg1, 1)}°C")
        print(f'The average windspeed is {round(avg2, 1)} km/h')

    
def average():
        while True:
            try:
                dys = input('Enter the number of days you wanna see the average of: ').lower()
                lines('kregg.csv', int(dys))
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
        print(f"The temperature is {temp}°C")
        print(f"The windspeed is {w_S} km/h")
        if day == 1:
            print('Day time')
        else: 
            print('Night time')
        with open('kregg.csv', 'a') as f:
            f.write(f'{c}:\n')
            f.write(f'The temperature is {temp}\n')
            f.write(f"The windspeed is {w_S} km/h\n")
            if day == 1:
                f.write(f'It was the day time when {c} was searched\n')
            else:
                f.write(f'It was the night time when {c} was searched\n')
    except requests.exceptions.RequestException:
        print("Check your connection sir!")
    except(KeyError, ValueError):
        print('City/country not found check the spelling!')



def lines(directory, num_of_days):
    the_floats = []
    tem = []
    w__s = []
    with open(directory) as f:
        reader = f.read().split()
        line_r = collections.deque(reader, num_of_days*19)#each country/city with one word name contains 19 words
        if num_of_days*19 > len(line_r):
            sys.exit('The file directory does not have this many days in it!')
        for i in line_r:
            try:
                the_floats.append(float(i))
            except ValueError:
                pass
        for y in the_floats[::2]:
            tem.append(y)
        for k in the_floats[1::2]:
            w__s.append(k)
        averg1 = sum(tem)/len(tem)
        averg2 = sum(w__s)/len(w__s)
        print(f'The average temperature in the last {num_of_days} day(s) is {round(averg1, 1)}°C')
        print(f'The average windspeed in the last {num_of_days} day(s) is {round(averg2, 1)} km/h')

funcs = {
    'total': total,
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