import sys
import csv


class Holder():
    def __init__(self, teacher, level, average=float):
        self.teacher = teacher
        self.level = level
        try:
            self.average = average
        except ValueError as e:
            raise e('The average should be a float!')
    def turn_to_dict(self):
        return {
            'teacher': self.teacher,
            'level': self.level,
            'average': self.average
        }


def review_test():
    teacher = input('Enter the teacher name: ')
    level = input('Enter the level: ')
    ans = []
    fieldnames = ['teacher', 'level', 'average']
    while True:
        correct_answers = input('Enter the total correct ans or q for quit: ').lower()
        if correct_answers == 'quit' or correct_answers == 'q':
            try:
                avg = round(sum(ans)/len(ans), 1)
                with open('polyg.csv', 'a') as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    # writer.writeheader()
                    hr = Holder(teacher, level, avg)
                    writer.writerow(hr.turn_to_dict())
                sys.exit(f'The average is {avg}%')
            except ZeroDivisionError:
                sys.exit('No data entered!')
        else:
            overall = int(correct_answers) / 0.7
            ans.append(overall)
            print(f"{round(overall, 1)}%")
            continue


def end_year():
    fieldnames = ['teacher', 'level', 'average']
    lst = []
    teacher = input('Enter the teacher name: ')
    level = input('Enter the level: ').capitalize()
    if level == 'A1' or level == 'A1+':
        while True:
            correct_ans = input('Enter the number of correct ans or q for quit: ')
            if correct_ans == 'q':
                try:
                    with open('end.csv', 'a') as f:
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
                        writer.writeheader()
                        avg = round(sum(lst)/len(lst), 1)
                        hr = Holder(teacher, level, avg)
                        writer.writerow(hr.turn_to_dict())
                    sys.exit(f'The class average is {avg}%')
                except ZeroDivisionError:
                    sys.exit('No data entered!')
            else:
                overall = int(correct_ans) * 70/80
                try:
                    speaking = int(input('Enter the speaking: '))
                    overall += speaking
                    ov = round(overall,1)
                    lst.append(ov)
                    print(f"{ov}%")
                    continue
                except ValueError:
                    print('Input an int')
                    continue


    if level == 'A2':
        while True:
            reading = input('Enter the reading: ').lower()
            listening = input('Enter the listening: ').lower()
            if reading == 'q' or listening == 'q':
                try:
                    with open('end.csv', 'a') as f:
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
                        writer.writeheader()
                        avg = round(sum(lst)/len(lst), 1)
                        hr = Holder(teacher, level, avg)
                        writer.writerow(hr.turn_to_dict())
                    sys.exit(f"The class avg {avg}%")
                except ZeroDivisionError:
                    sys.exit('No data entered!')
            else:
                try:
                    lr = int(reading) + int(listening)
                except ValueError:
                    print('The last input was not an int!')
                    continue
                pre_total = lr * 0.9
                while True:
                    writing = input('Enter the writing: ')                    
                    speaking = input("Enter the speaking: ")
                    if writing == 'q' or speaking == 'q':
                        try:
                            sys.exit(f'The class average is {avg}%')
                        except ZeroDivisionError:
                            sys.exit('No data entered!')
                    try:
                        total = pre_total + int(writing) + int(speaking)
                        lst.append(total)
                        print(f"{round(total, 1)}%")
                        break
                    except ValueError:
                        print('The last input was not an int!')
                        continue
    

    if level == 'B1':
        while True:
            reading = input('Enter the reading: ').lower()
            listening = input('Enter the listening: ').lower()
            if reading == 'q' or listening == 'q':
                try:
                    with open('end.csv', 'a') as f:
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
                        writer.writeheader()
                        avg = round(sum(lst)/len(lst), 1)
                        hr = Holder(teacher, level, avg)
                        writer.writerow(hr.turn_to_dict())
                    sys.exit(f"The class avg {avg}%")
                except ZeroDivisionError:
                    sys.exit('No data entered!')
            else:
                try:
                    lr = int(reading) + int(listening)
                except ValueError:
                    print('The last input was not an int!')
                    continue
                pre_total = lr / 1.14
                while True:
                    writing = input('Enter the writing: ')                    
                    speaking = input("Enter the speaking: ")
                    if writing == 'q' or speaking == 'q':
                        try:
                            sys.exit(f'The class average is {avg}%')
                        except ZeroDivisionError:
                            sys.exit('No data entered!')
                    try:
                        total = pre_total + int(writing) + int(speaking)
                        lst.append(total)
                        print(f"{round(total, 1)}%")
                        break
                    except ValueError:
                        print('The last input was not an int!')
                        continue
    

    if level == 'B1+':
        while True:
            reading = input('Enter the reading: ').lower()
            listening = input('Enter the listening: ').lower()
            if reading == 'q' or listening == 'q':
                try:
                    with open('end.csv', 'a') as f:
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
                        writer.writeheader()
                        avg = round(sum(lst)/len(lst), 1)
                        hr = Holder(teacher, level, avg)
                        writer.writerow(hr.turn_to_dict())
                    sys.exit(f"The class avg {avg}%")
                except ZeroDivisionError:
                    sys.exit('No data entered!')
            else:
                try:
                    lr = int(reading) + int(listening)
                except ValueError:
                    print('The last input was not an int!')
                    continue
                pre_total = lr * 0.84
                while True:
                    writing = input('Enter the writing: ')                    
                    speaking = input("Enter the speaking: ")
                    if writing == 'q' or speaking == 'q':
                        try:
                            sys.exit(f'The class average is {avg}%')
                        except ZeroDivisionError:
                            sys.exit('No data entered!')
                    try:
                        total = pre_total + int(writing) + int(speaking)
                        lst.append(total)
                        print(f"{round(total, 1)}%")
                        break
                    except ValueError:
                        print('The last input was not an int!')
                        continue
    
                    
    if level == 'B2':
        while True:
            reading = input('Enter the reading: ').lower()
            listening = input('Enter the listening: ').lower()
            if reading == 'q' or listening == 'q':
                try:
                    with open('end.csv', 'a') as f:
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
                        writer.writeheader()
                        avg = round(sum(lst)/len(lst), 1)
                        hr = Holder(teacher, level, avg)
                        writer.writerow(hr.turn_to_dict())
                    sys.exit(f"The class avg {avg}%")
                except ZeroDivisionError:
                    sys.exit('No data entered!')
            else:
                try:
                    lr = int(reading) + int(listening)
                except ValueError:
                    print('The last input was not an int!')
                    continue
                pre_total = lr * 0.64
                while True:
                    writing = input('Enter the writing: ')                    
                    speaking = input("Enter the speaking: ")
                    if writing == 'q' or speaking == 'q':
                        try:
                            sys.exit(f'The class average is {round(avg, 1)}%')
                        except ZeroDivisionError:
                            sys.exit('No data entered!')
                    try:
                        total = pre_total + int(writing) + int(speaking)
                        lst.append(total)
                        print(f"{round(total, 1)}%")
                        break
                    except ValueError:
                        print('The last input was not an int!')
                        continue

dict_ = {
    'review': review_test,
    'end': end_year,
    '-h': lambda : [print("*",i) for i in dict_.keys()]
}


def main():
    if len(sys.argv) < 2:
        sys.exit('Exit for now later fix to something better, -h for help!')
    else:
        command = dict_.get(sys.argv[1].lower())
        if command:
            command()
        else:
            print('Command not found, -h for help')

#level control could be improved instead of using if and if and if I think this could be improved somehow
#the project is not fully complete yet
if __name__ == '__main__':
    main()