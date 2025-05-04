import csv

with open('people.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['Name'], row['Age'])

with open('people2.csv','w',newline='') as f:
    writer = csv.DictWriter(f,fieldnames=['Name', 'Age'])
    writer.writeheader()
    writer.writerow({'Name': 'Carol', 'Age':28})