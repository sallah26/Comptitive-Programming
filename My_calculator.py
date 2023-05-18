def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
list_of_opperation=["-","+","*","/"]

def calculator():
    x=int(input("Enter the first number: "))
    for i in list_of_opperation:
        print(i)
    opp=str(input("Which opperation you want to perform?:"))
    if opp=="-" or "+" or "*" or "/":
        c=5
    else:
        print("Invalid input")
        exit()
    y=int(input("Enter the second number: "))
    if opp=="+":
        print("their addition is: ",add(x,y))
    elif opp=="*":
        print("their multiplication is: ",mul(x,y))
    elif opp=="-":
        print("their subtraction is: ",sub(x,y))
    elif opp=="/":
        print("their division is: ",div(x,y))
    else:
        print("invalid input!")
calculator()
while True:
    strr=str(input("Do you want to calculate anymore? enter 'Y' for yes 'N' for no: "))
    if strr =="y":
        calculator()
    else:
        print("Thanks for working with us!")
        exit()

