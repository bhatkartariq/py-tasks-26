balance =100000
correct_pin=1504
def check_balance():
    print(f"Your Account balance sir:{balance}")
    
def deposit(amount):
    global balance
    
    if amount>0:
        
        balance=balance+amount
        print("your money has been deposited !!")
        
        check=input("Do you want to check balance: (y/n)\n")
        if check=="y":
            print(f"The balance now is :{balance}\n")
        else:
            print("invalid option\n")
    else:
        print("invalid amount\n")


def withdraw(amount):
    global balance
    if amount>0 and balance>0:
        balance=balance-amount
        print("amount has been withdrawn !!")
        check=input("Do you want to check balance: (y/n)")
        if check=="y":
            print(f"The balance now is :{balance}\n")
           
        else:
            print("invalid option")
    else:
        print("NO BALANCE!! deposit money first\n")

    
def authenticate(pin):
    if pin==correct_pin:
        return True
    else:
        return False
def more(check):
    
    if check=="y":
        check_balance()
    elif check=="n":
        main_menu()
    else:
        print("Invalid option!!")
def main_menu():
    attempts=3
    while attempts>0:
        pin=int(input("Enter your 4 digit pin: "))
        if authenticate(pin):
            print("AUTHENTICATION CORRECT!!")
            print("------WELCOME SIR/MADAM------\n")
            break
        else:
            attempts-=1
            print("Incorrect pin attempts remaining",attempts)
        if attempts==0:
            print( "all attempts has ben used !! your card has been BLOCKED!!!")
            return
    while True:
        print("------MENU------\n")
        print("1. Check balance")
        print("2. Withdraw Cash")
        print("3. Deposoit ")
        print("4. exit")
        
        choice=input("enter your choice: ")

        if choice=="1":
            check_balance()

        elif choice=="2":
            withdraw_amount=float(input("Enter the amount to withdraw: "))
            withdraw(withdraw_amount)
            print("Please!! collect the cash\n")
            
            
            
            
        elif choice=="3":
            amount=float(input("Enter the amount to deposit: "))
            deposit(amount)
            
            
        elif choice=="4":
            break
        else:
            print("invalid option\n")
main_menu()