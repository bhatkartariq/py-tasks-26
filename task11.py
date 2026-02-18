#Aim: WAP to find the greatest of three numbers entered by user.
a,b,c=map(int,input("enter numbers(seprated by spaces): ").split())
if a>b and a>c:
    great=a
elif b>c and b>a:
    great=b
else:
    great=c
print(f"greatest:{great}")
