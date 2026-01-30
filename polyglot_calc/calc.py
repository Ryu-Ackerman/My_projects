import sys


def review_test():
    ans = []
    while True:
        correct_answers = input('Enter the total correct ans or q for quit: ').lower()
        if correct_answers == 'quit' or correct_answers == 'q':
            avg = sum(ans)/len(ans)
            sys.exit(f'The average is {round(avg, 1)}%')
        else:
            overall = int(correct_answers) / 0.7
            ans.append(overall)
            print(f"{round(overall, 1)}%")
            continue


def end_year():

    level = input('Enter the level: ').capitalize()
    if level == 'A1':
        while True:
            correct_ans = input('Enter the number of correct ans or q for quit: ')
            if correct_ans == 'q':
                sys.exit()
            else:
                overall = int(correct_ans) * 70/80
                try:
                    speaking = int(input('Enter the speaking: '))
                    overall += speaking
                    print(f"{round(overall), 1}%")
                    continue
                except ValueError:
                    print('Input an int')
                    continue


    if level == 'A2':
        while True:
            reading = input('Enter the reading: ').lower()
            listening = input('Enter the listening: ').lower()
            if reading == 'q' or listening == 'q':
                sys.exit("You successfully quit the program!")
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
                        sys.exit('You successfully quit the program!')
                    try:
                        total = pre_total + int(writing) + int(speaking)
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
                sys.exit("You successfully quit the program!")
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
                        sys.exit('You successfully quit the program!')
                    try:
                        total = pre_total + int(writing) + int(speaking)
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


if __name__ == '__main__':
    main()
    #find the formulas for b1, a1+, b1+