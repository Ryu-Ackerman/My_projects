import csv
import sys



class Holder():
    def __init__(self, teacher, level, average):
        self.teacher = teacher
        self.level = level
        self.average = average
    def turn_to_dict(self):
        return {
            'teacher': self.teacher,
            'level': self.level,
            'average': self.average
        }
    
class Save():
    def __init__(self, teacher, level, average):
        self.teacher = teacher
        self.level = level
        self.average = average
    def save_file(self):
        fieldnames = ['teacher', 'level', 'average']
        with open('end.csv', 'a') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
    
LEVELS = {
    'A2': 0.9,
    'B1': 1/1.14,
    'B1+': 0.84,
    'B2': 0.64
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



def a1_end(level, teacher):
    fieldnames = ['teacher', 'level', 'average']
    lst = []
    if level == 'A1' or level == 'A1+':
        while True:
            correct_ans = input('Enter the number of correct ans or q for quit: ')
            if correct_ans == 'q':
                try:
                    with open('end.csv', 'a') as f:
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
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


def handle_levels(level, teacher):
    lst = []
    fieldnames = ['teacher', 'level', 'average']
    multiplier = LEVELS.get(level)
    while True:
            reading = input('Enter the reading: ').lower()
            listening = input('Enter the listening: ').lower()
            if reading == 'q' or listening == 'q':
                try:
                    with open('end.csv', 'a') as f:
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
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
                pre_total = lr * multiplier
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


def end_of_year():
    teacher = input("Enter the teacher's name: ")
    level = input('Enter the level: ').capitalize()
    if level in LEVELS:
        handle_levels(level, teacher)
    elif level in ('A1', 'A1+'):
        a1_end(level, teacher)
    else:
        sys.exit('Uknown level!')

dict_ = {
    'end': end_of_year,
    'review': review_test,
    '-h': lambda : [print("*",i) for i in dict_.keys()]
}

def main():
    if len(sys.argv) < 2:
        sys.exit('No enough arguments on the terminal!' \
        '-h for help')
    command = dict_.get(sys.argv[1].lower())
    if command:
        command()
    else:
        sys.exit('Uknown command!' \
        '-h for help')

if __name__ == '__main__':
    main()