 #if else conditions

print("welcome to the rollercoaster!")
height=int(input("What is your height in cm? "))
age=int(input("what is your age? "))
if height >=120:
    print("You can ride the rollercoaster")
    if age <12:
        print("Please pay $5.")
    elif age <=18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to get taller before you can ride")

#3.1 exercise odd or even
number = int(input("Please enter a number: "))
if number %2==0:
    print("Number is even")
else:
    print("Number is odd")
#3.2 exercise bmi upgraded version
height= float(input("enter your height in m: "))
weight= float(input("what is  your weight in kg: "))
bmi = round(weight / height*height)
if bmi <=18.5:
    print(f"Your BMI is {bmi} and you are underweight")
elif  bmi < 25:
    print(f"Your BMI is {bmi} and you are normal weight")
elif bmi <30:
    print(f"Your BMI is {bmi} and you are overweight")
elif bmi <35:
    print(f"Your BMI is {bmi} and you are obese")
else:
    print(f"Your BMI is {bmi} and you are clinicaly obese")

#3.3 exercise leap year
year = int(input("Enter year you wish to check: "))
if year %4 ==0:
    print("It is a leap year")
elif year %100==0:
    print("It is a leap year")
elif year % 400==0:
    print("It is a leap year")
else:
    print("It is not a leap year")        






