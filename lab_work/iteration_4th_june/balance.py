# Bank Management Program

balance = 10000

while True:
    print("\n----- MENU -----")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance = ₹", balance)

    elif choice == 2:
        amount = float(input("Enter amount to deposit: ₹"))
        balance += amount
        print("Amount Deposited Successfully!")
        print("Updated Balance = ₹", balance)

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: ₹"))

        if amount <= balance:
            balance -= amount
            print("Withdrawal Successful!")
            print("Remaining Balance = ₹", balance)
        else:
            print("Insufficient Balance!")

    elif choice == 4:
        print("Thank You! Exiting Program...")
        break

    else:
        print("Invalid Choice! Please try again.")