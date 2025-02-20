import random
number = random.randint(10,20)
print("Guess my number 10 thorugh 20.")
if number%2==0:
    print("A hint is the number is even.")
else:
    print("A hint is the number is odd. ")
while True:
    guess = int(input("Enter your guess: "))
    if number ==  guess:
        print("You have guessed correctly.")
        break
    else:
        print("Your guess is incorrect;try again.")
