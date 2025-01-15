print('Hello')
print("welcome to the tip calculator")
bill=float(input("what is the total tip bill?"))
tip=int(input("how much %tip do you want to pay?"))
tip_percent = tip/100
total_tip_amt = bill*tip_percent
people=int(input("how many people to split the bill?"))
total_bill = bill+total_tip_amt
bill_per_person = total_bill/people
final_amt = round(bill_per_person, 2)
print(f"each person should pay {final_amt}")