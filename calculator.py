# Write a program to make a calculator : For making a calculator create four functions add, subtract, multiply, divide. Ask for a choice from users which operation they want to perform. Take user input whatever operation they want to perform And call that function accordingly.
def Add(a,b):
    return a+b
def Multiply(a,b):
    return a*b
def Divide(a,b):
    return a/b
def Minus(a,b):
    return a-b
userinput = input("Which operators would you like to choose; a for add, s for subtraction, m for multiplication or d for division? ").upper()
number1 = int(input("What number you like to be included? "))
number2 = int(input("What number you like to be included aswell? "))
if  userinput == "A":
    print("The sum of the numbers are",Add(number1,number2),end=".")
elif  userinput == "S":
    print("The difference of the numbers are",Minus(number1,number2),end=".")#
elif  userinput == "M":
    print("The product of the numbers are",Multiply(number1,number2),end=".")
elif  userinput == "D":
    print("The quotient of the numbers are",Divide(number1,number2),end=".")
else:
    print("Invalid.")