numbers = [2,4,5,4,7,8,9,2,1,11,23,1,0]

largest = 0
for number in numbers:
    if number > largest:
        largest = number
print(f"largest number is {largest}")