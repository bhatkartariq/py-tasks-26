#Aim: WAP to find average of list of numbers entered by
#  the user by single input statemen
a = input("Enter numbers separated by space: ").split()

numbers = list(map(int, a))


average = sum(numbers) / len(numbers)

print("Average =", average)
