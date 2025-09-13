from add import sum
from sub import sub
from mul import mul
from divion import div

while True:
    a = int(input("Enter the first number: "))
    op = input("Enter an operator (+, -, *, /): ")
    b = int(input("Enter the second number: "))
    
    if op == "+":
        print("Result:", sum(a, b))
    elif op == "-":
        print("Result:", sub(a, b))
    elif op == "*":
        print("Result:", mul(a, b))
    elif op == "/":
        print("Result:", div(a, b))
    else:
        print("Invalid operator! Please use +, -, *, or /.")
    
    choice = input("Do you want to quit? (y/n): ").lower()
    if choice == "y" or choice == "yes":
        print("Exiting the calculator. Goodbye!")
        break
    elif choice == "n" or choice == "no":
        print("Continuing...\n")
    else:
        print("Invalid choice. Calculator will continue.\n")
