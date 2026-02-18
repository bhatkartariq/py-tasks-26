#Aim: Write a program to Read two numbers and s
# wap them without using a third variable
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

num1,num2=num2,num1

print(f"After swapping:{num1,num2}")

