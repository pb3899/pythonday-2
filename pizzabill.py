# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
bill =0
#Write your code below this line 👇
if size=="S":
  bill=15
  if add_pepperoni =="Y":
    bill=17
    if extra_cheese =="Y":
      bill=18
      print(f"your BILL is ${bill}" )
    else: 
     print(f"your BILL is ${bill}")
  else:
    print(f"your BILL is ${bill}")
elif size=="M":
  bill=20
  if add_pepperoni =="Y":
    bill=23
    if extra_cheese =="Y":
      bill=24
      print(f"your BILL is ${bill}" )
    else: 
     print(f"your BILL is ${bill}")
  else:
    print(f"your BILL is ${bill}")
elif size=="L":
  bill=25
  if add_pepperoni =="Y":
    bill=28
    if extra_cheese =="Y":
      bill=29
      print(f"your BILL is ${bill}" )
    else: 
     print(f"your BILL is ${bill}")
  else:
    print(f"your BILL is ${bill}")
else:
  print("enter proper order")
