# CIS 103: Introduction to Programming
# Lab 01: "Calculator Function"
# Instructor: Md Ali
#Ndubuisi mbamalu
# Date: 9/14/2024
#

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero!."


def main():
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '5':
            print("exiting, thank you!")
            break

        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} + {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} + {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"{num1} + {num2} = {divide(num1, num2)}")
        else:
            print("Invalid input")

#1This is a calculator program that allows the user to perform the following three operations.

def exponent(x, y):
    return x ** y
def modulus(x, y):
    return x % y
def square_root(x):
    return (x)
print("1. Exponent")
print("2. Modulus")
print("3. Square root")

choice = input("Enter choice")

if choice == '1':
        x = float(input("Enter base (x): "))
        y = float(input("Enter exponent (y): "))
        print(f"{x} ^ {y} = {exponent(x, y)}")

elif choice == '2':
        x = float(input("Enter number (x): "))
        y = float(input("Enter divisor (y): "))
        print(f"{x} % {y} = {modulus(x, y)}")

elif choice == '3':
        x = float(input("Enter number (x): "))
        print(f"√{x} = {square_root(x)}")

else:
        print("Invalid Input")
#Instructions:
#The user selects an operation by typing in #s 1,2,3.
#After choosing an operation, the user enters the required input numbers.
#The program displays the result, then asks if the user wants to perform another calculation or exit.
#The screen clears between operations for a clean interface.

#2 and 3, Ask if the user wants to continue or clear the screen
        next_action = input("\nDo you want to perform another calculation? (y/n): ").lower()
        if next_action != 'y':
            print("Thank you for nothing!")
