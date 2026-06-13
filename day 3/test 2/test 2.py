a=int(input("enter a number: "))
b=int(input("enter another number: "))
choice=input("enter your preferred operation:add/subtract/multiply/divide: ")
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
if choice == "add":
    print(add(a,b))
elif choice == "subtract":
    print(subtract(a,b))
elif choice == "multiply":
    print(multiply(a,b))
elif choice == "divide":
    print(divide(a,b))
else:
    print("you've given an invalid choice")
    