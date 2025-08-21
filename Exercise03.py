balance = 1000

while True:
    user_input = input("Enter deposit, withdraw, check_balance, or exit: ")

    if user_input == "deposit":
        amount = int(input("Amount: "))
        balance += amount
        print("Balance:", balance)

    elif user_input == "withdraw":
        amount = int(input("Amount: "))
        if amount > balance:
            print("Not enough balance!")
        else:
            balance -= amount
            print("Balance:", balance)

    elif user_input == "check_balance":
        print("Balance:", balance)

    elif user_input == "exit":
        print("Goodbye")
        break

    else:
        print("Invalid option")