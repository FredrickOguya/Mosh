# 💻 Your Practice Task
# ✅ Write a script that:
# 1️⃣ Creates a CSV file students.csv with header: Name, Grade
# 2️⃣ Adds 3 students and their grades
# 3️⃣ Reads and prints each row

import csv

with open('students.csv','w')as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Grade'])
    writer.writerow(['Christian', 'A'])
    writer.writerow(['Onyango', 'A'])
    writer.writerow(['Fredi', 'B'])

with open('students.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)