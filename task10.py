#Aim: WAP to find if a string entered by user is a palindrome or not.
word=input("enter the word: ")
reverse=word[::-1]

if word==reverse:
    print(" it is a palindrome")
else:
    print("its not a palindrome")
