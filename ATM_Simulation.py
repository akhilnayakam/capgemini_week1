def check_balance(balance):
    print(f"Your current balance is: {balance}")

def deposit_money(balance):
    while True:
        amount = float(input("Enter the amount to deposit: "))
        if amount <= 0:
            print("Please enter a positive amount.")
        else:
            balance += amount
            print(f"{amount} deposited successfully. New balance: {balance}")
            break
        return balance

def withdraw_money(balance):
    while True:
        amount = float(input("Enter the amount to withdraw: "))
        
        if amount <= 0:
            print("Please enter a positive amount.")
        elif amount > balance:
            print("Insufficient balance. Please try a smaller amount.")
        else:
            balance -= amount
            print(f"{amount} withdrawn successfully. Remaining balance: {balance}")
            break


def atm():
    print("Welcome to the ATM!")
    balance = 0.0
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                check_balance(balance)
            elif choice == 2:
                balance = deposit_money(balance)
            elif choice == 3:
                balance = withdraw_money(balance)
            elif choice == 4:
                print("Thank you for using the ATM!")
                break
            else:
                print("Invalid option. Please select a number between 1 and 4.")
        else:
            print("Invalid input. Please enter a number.")

atm()
