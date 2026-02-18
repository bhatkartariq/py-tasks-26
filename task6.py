#Aim: Write a program to find the two sides of a right angle triangle if 
#hypotenuse and one angle in degrees is given by the user.
import math

hypotenuse = float(input("Enter the hypotenuse: "))
angle = float(input("Enter the angle (in degrees): "))

opposite = hypotenuse * math.sin(math.radians(angle))
adjacent = hypotenuse * math.cos(math.radians(angle))

print("The other two sides are:")
print("Opposite side =", opposite)
print("Adjacent side =", adjacent)
