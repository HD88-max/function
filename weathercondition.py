#Weather condition
#Outline:
#Write a program to display the weather in autumn and spring :
weather = input("Is it Autumn or Spring? ").lower()
def Autumn(weather):
    print("It could be cold or leafy because it is",weather,end=".")
def Spring(weather):
    print("It could be warm or windy because it is",weather,end=".")

if weather == "spring":
    Spring(weather)
elif weather == "Autumn":
    Autumn(weather)
else:
    print("It is either summer or winter. ")