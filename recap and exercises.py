# 🧠 Exercise 1: Handle Division by Zero
# Task:
# Write a program that takes two numbers from the user and divides them. Handle the case where the denominator is zero.

# Template:

# python
# Copy code
# # Your code here


# Add try-except to handle division
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1/num2
except ZeroDivisionError:
    print("the second number canot be zero")
