def total_cal(bill,tip_per):
    total_bill = bill +((bill*tip_per)//100)
    print(total_bill)
total_cal(100,20)