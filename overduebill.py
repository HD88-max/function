def total_bill(n):
    print("You need to pay {0}".format(n))
def paid(y):
    print("You have paid {0}".format(y))
y = int(input("How much have you paid"))
n = int(input("How much is the total cost?"))
print(total_bill(n))
print(paid(y))
if n > y:
    tip = n - y
    yn = input("Do you want to pay £",tip,end="(y for yes and n for no)?").upper()
    if yn == "Y":
        print("Thank you for your tip.")
    elif yn == "N":
        print("Ok have a great day.")  
    else:
        print("Say yes or no.")
else:
    overdue = y - n
    print("You have £",overdue,"to pay.")