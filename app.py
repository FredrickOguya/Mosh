# numbers = [1,2]

# print(numbers[3])


try:
    age = int(input("Age:"))
except ValueError as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown")
print("Execution continues.")

