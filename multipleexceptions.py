# Write a program to check how the exceptions and finally statement works

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    if num1 % num2 == 0:
        print(f"{num1} is divisible by {num2}.")
    else:
        raise ValueError
except ValueError:
    print("There is a value error.")
except ZeroDivisionError:
    print("A zero division error has occured.")
else:
    print("No exceptions.")
finally:
    print("This will excecute.")