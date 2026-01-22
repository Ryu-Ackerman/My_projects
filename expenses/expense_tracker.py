import sys
import csv
from datetime import datetime
import collections
import json
import pytz



class Local:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


timezone = pytz.timezone("Asia/Samarkand")
date_s = datetime.now(timezone)
local = Local(date_s.year, date_s.month, date_s.day)


if local.month < 10:
    local.month = f"0{local.month}"
if local.day < 10:
    local.day = f"0{local.day}"
local_ = f"{local.year}-{local.month}-{local.day}"
        

class Transaction:
        def __init__(self, category, amount, date_s):
            self.category = category
            try:
                self.amount = float(amount)
            except ValueError as e:
                raise e('Input an int')
            self.date_s = date_s
        def turn_dict(self):
            return {
                "category": self.category,
                "amount": self.amount,
                "date": self.date_s
            }
        

def get_data():
    fi = input('For: ')
    se = input('Amount: ')
    return fi, se


def how_much():
    days = int(input("Enter the number of days you wanna see: "))
    lst = []
    nums = []
    with open('tracker.csv') as f:
        reader = csv.DictReader(f)
        lines = collections.deque(reader, days)
        for i in lines:
            lst.append(i['amount'])
        for x in lst:
            try:
                x = float(x)
                nums.append(x)
            except ValueError:
                    pass
        total = sum(nums)
        med = sum(nums)/len(nums)
        print("Here is your recorded expenditure:")
        print(f"The total amount: {total}")
        print(f'Normally how much you spent: {round(med, 1)}')


def new():
    while True:
        with open("tracker.csv", 'a', newline="") as f:
            fieldnames = ['category', 'amount','date']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            category, amount= get_data()
            t = Transaction(category, amount, local_)
            # writer.writeheader()
            writer.writerow(t.turn_dict())
        with open('category.json') as f:
            fjson = json.load(f)
            if category in fjson:
                namount = fjson[category]['amount'] + float(amount)
            else:
                namount = float(amount)
            fjson['total_money']['amount'] -= float(amount)
            fjson[category] = {
                'amount': namount
                }
            with open('category.json', 'w') as f:
                json.dump(fjson, f, indent=4)
        try:
            with open('date.json') as f:
                reader = json.load(f)
        except (FileNotFoundError,json.JSONDecodeError):
            reader = {}
        famount = float(amount)
        if str(local.day) in reader:
            famount += reader[str(local.day)]['amount']
        reader[str(local.day)] = {
            'amount': famount
            }
        with open('date.json', 'w') as f:
            json.dump(reader, f, indent=4)
            break

        
def add():
    with open("category.json") as f:
        dict_ = json.load(f)
        user = float(input('Enter the amount you wanna add: '))
        dict_['total_money']['amount'] += user
    with open('category.json', "w") as f:
        json.dump(dict_,f, indent=4)


funcs = {
    'last': how_much,
    'add': add,
    'new': new,
    '-h': lambda: [print('*',i) for i in funcs.keys()]
}


def main():
    if len(sys.argv) < 2:
        sys.exit('Not enough arguments on the terminal!\n -h for help`')
    command = funcs.get(" ".join(sys.argv[1:]))# .get() returns boolean or None
    if command:
        command()
    else:
        sys.exit('Uknown function!')


if __name__ == "__main__":
    main()