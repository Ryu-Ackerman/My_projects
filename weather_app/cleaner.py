import csv
columns = ['city', 'temperature', 'windspeed', 'date-time']
def clean():
    lines = []
    with open('kregg.csv') as f:
        reader = csv.DictReader(f)
        for i in reader:
            lines.append(i)
        if len(lines) > 30:
            lines.pop(0)
    with open('kregg.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=columns)
        writer.writeheader()
        for i in lines:
            writer.writerow(i)