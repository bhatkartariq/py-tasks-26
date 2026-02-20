#Aim: WAP to read a comma seperated string of numbers as input and
#  generate a new list with even indexes squared and odd indexes cubed.
nums = list(map(int, input("Enter numbers separated by commas: ").split(",")))

result = [nums[i]**2 if i % 2 == 0 else nums[i]**3 for i in range(len(nums))]

print(result)


