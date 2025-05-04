import json

grades = {
    'Fred':'B',
    'Christian' : 'A',
    'Onyango':'A+'
}

with open('grades.json', 'w') as f:
    json.dump(grades,f)


with open('grades.json') as f:
    data = json.load(f)
    print(data)