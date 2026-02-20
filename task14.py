#Write a program that keeps multiplying the digits 
#of a number until a single digit is obtained.
#  Count how many iterations were required
nums = int(input("Enter a number: "))
Iteration = 0
while nums >= 10: 
    product = 1
    for digit in str(nums):
        product *= int(digit)
    nums = product
    Iteration += 1

print("Single digit:", nums)
print("Iterations:", Iteration)
