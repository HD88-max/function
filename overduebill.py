def total_bill(n):
    print("You need to pay {0}".format(n))
def paid(y):
    print("You have paid {0}".format(y))
bill = int(input("How much is the total bill?"))
payment = int(input("How much have you paid"))
print(total_bill(bill))
print(paid(payment))
if bill > payment:
    tip = payment-bill
    balance=bill-payment
    response = input("Do you want to pay tip (y for yes and n for no)?").upper()
    if response == "Y":
        print(f"Thank you for your tip {tip} ")
    else:
        print(f"Your balance is {balance}. have a great day.")  
else:
    overdue = bill - payment
    print("You have £",overdue,"to pay.")