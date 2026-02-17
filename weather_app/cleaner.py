import csv
columns = ['city', 'temperature', 'windspeed', 'date-time']
def clean():
    lines = []
    with open('kregg.csv') as f:
        reader = csv.DictReader(f)
        for i in reader:
            lines.append(i)
        if len(lines) > 30:#if the number of searches exceed 30 delete one from the top of csv file
            lines.pop(0)#remove the first item
    with open('kregg.csv', 'w', newline='') as f:#writing over the csv after storing everything to a list and modifying it
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for i in lines:
            writer.writerow(i)