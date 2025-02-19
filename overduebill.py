def total_bill(bill):
    print("You need to pay {0}".format(bill))
def paid(payment):
    print("You have paid {0}".format(payment))
bill = int(input("How much is the total bill? "))
payment = int(input("How much have you paid "))
tip = bill - payment
print(total_bill(bill))
print(paid(payment))
if bill > payment:
    balance=bill-payment -tip
    response = input(f"Do you want to pay a tip of {tip} (y for yes and n for no)? ").upper()
    if response == "Y":
        print(f"Thank you for your tip of {tip} ")
    else:
        print(f"Your balance is {balance - tip}.Have a great day.")  
else:
    overdue = bill - payment
    print("You have £",overdue,"to pay.")