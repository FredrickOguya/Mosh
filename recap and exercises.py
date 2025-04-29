try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter the second number: "))

    soln = num1/num2

    print(f"{num1}/{num2} = {soln}")
except ValueError:
    print("Enter a valid number")
except ZeroDivisionError:
    print("The second number cannot be zero")

finally:
    print("program successfull")