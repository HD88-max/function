try:
    age = int(input("Enter you age: "))
    if age >= 18:
        print("You have valid access.")
    elif age < 18:
        age2 = 18 -  age 
        print(f"You are {age} years old.You have {age2} years left till valid access")
    else:
        raise ValueError
except ValueError as h:
    print("You have entered something wrong.Please check your age and try again.")
finally:
    print("Enjoy no matter what lays ahead of you.")