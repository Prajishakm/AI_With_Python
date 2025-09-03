prices = [10,14,22,33,44,13,22,55,66,77]
total = 0

print("Supermarket")
print("===========")

while True:
    user_input = int(input("Please select product (1-10) 0 to Quit: "))

    if user_input == 0:
        break

    if 1 <= user_input <= 10:
        price = prices[user_input - 1]
        total += price
        print("Product:", user_input, "Price:", price)
    else:
        print("Incorrect selection.")

print("Total:", total)

payment = int(input("Payment: "))
change = payment - total
print("Change:", change)