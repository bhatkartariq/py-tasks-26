#Aim: Write a program to find the solutions to a quadratic equation
#ax^2 + bx + c = 0. Take a, b, c from User. Assume only real solutions.
a = int(input("ENTER THE COEFFICIENT OF X^2: "))
b = int(input("ENTER THE COEFFICIENT OF X: "))
c = int(input("ENTER THE CONSTANT: "))

discriminant = b**2 - 4*a*c

root1 = (-b + discriminant**0.5) / (2*a)
root2 = (-b - discriminant**0.5) / (2*a)

print("The real solutions are:", root1, ",", root2)
