user_input = int(input("enter a number: "))
print(f"Multiplication table for the {user_input} numbers:")
for i in range(1, 11):
    print(f"{user_input} x {i} = {user_input * i}")
