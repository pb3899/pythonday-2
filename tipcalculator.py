bill=float (input("please enter total bill $"))
ppl=int (input("total no of ppl splitting bill "))
tip=int (input("% of tip you wanna give 10 or 12 or 15 "))
TIP=(bill/ppl)*(tip/100)
amount=round((bill/100)+TIP ,2)
print(f"each person should pay $ {amount}")


bill=float (input("please enter total bill $"))
ppl=int (input("total no of ppl splitting bill "))
tip=int (input("% of tip you wanna give 10 or 12 or 15 "))
TIP=(bill/ppl)*(tip/100)
amount="{:.2f}".format((bill/100)+TIP)
print(f"each person should pay $ {amount}")
