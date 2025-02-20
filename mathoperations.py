import math
number = float(input("Enter a decimal value: "))
print(f"The floor value of {number} is {math.floor(number)}")
print("The ceil value of {0} is {1}.".format(number,math.ceil(number)))
x = float(input("Enter a value: "))
y = float(input("Enter a negative value: "))
print("The copysign of {0} and {1} is {2}.".format(x,y,math.copysign(x,y)))
square = float(input("Enter a value: "))
print("The sqaure root of {0} is {1}.".format(square,math.sqrt(square)))