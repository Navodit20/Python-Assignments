                                #Assignment 1
#Name: Navodit Gupta
#SID: 21107082
#Branch: Mechanical

#Q1
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))

avg = (num1 + num2 + num3)/3
print(avg)

#Q2
gross_income = float(input("Enter gross income to the nearest penny:"))
std_deduction = 10000 #standard deduction
dependent = 3000 #dependent deduction
num_dependent = int(input("Enter number of dependents:"))
taxable_income = gross_income - std_deduction - (dependent * num_dependent)
tax_rate = 0.2
tax = taxable_income * tax_rate 
print("Income tax:",tax)

#Q3
num_sec = int(input("Enter number of seconds: "))
minute = num_sec//60
sec = num_sec%60
print(f"That's {minute} minutes and {sec} seconds")

#Q4
a = '25'
b = 25
c = 25.0
d = str(int(a) + b + int(c))
print(f"{d}, this is",type(d))

#Q5
import math

for i in range(0,360,15):
    sin = math.sin(i*math.pi/180)
    cos = math.cos(i*math.pi/180)
    print(i,'---',round(sin,4),round(cos,4))


