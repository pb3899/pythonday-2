# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi=weight/(height**2)
if bmi<= 18.5:
  print("ur underweight")
elif bmi<=25:
  print("your weight is normal")
elif bmi<=30:
 print("ur overweight")
elif bmi<=35:
  print("ur obese")
else:
  print("ur clinically obese")
