import csv

with open('people.csv', 'w', newline ='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name','Age'])
    writer.writerow(['Alice',30])
    writer.writerow(['Bob', 25])