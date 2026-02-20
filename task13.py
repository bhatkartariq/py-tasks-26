#Aim: WAP to find the double factorial of a number.
num=int(input("enter a number :  "))
factorial=1
for i in range(num,0,-2):
    factorial*=i
print(f"double factorial : {factorial}")