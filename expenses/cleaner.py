import json
import pytz
from datetime import datetime
import requests

def clean():
    r = requests.get('https://ipinfo.io/json')
    j = r.json()

    zone = j['timezone']

    timezone = pytz.timezone(zone)

    date = datetime.now(timezone)

    MONTHS = {'1': 'Jan', '2': 'Feb', '3': 'Mar', '4': 'Apr',
            '5': 'May','6': 'Jun', '7': 'Jul','8': 'Aug',
            '9': 'Sep','10': 'Oct','11': 'Nov','12': 'Dec'
    }

    with open('date.json') as f:
        reader = json.load(f)
        for i in reader:
            if str(date.month) != i:
                reader = {
                    f'{date.month}': {
                        'month': MONTHS[f'{date.month}']
                    }
                }
                with open('date.json', 'w') as file:
                    json.dump(reader, file ,indent=4)
            else:
                pass