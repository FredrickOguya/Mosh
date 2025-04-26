# numbers = [1,2]

# print(numbers[3])


try:
    age = int(input("Age:"))
    exfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age.")
else:
    print("No exceptions were thrown")

