age = int(input("Enter your age: "))
citizenship = input("Enter your citizenship (yes/no): ")

if citizenship == "yes" and age >= 18:
    print("You have the right to vote")
elif age < 18:
    years_left = 18 - age
    print(f"You are not old enough to vote. You need to wait {years_left} more year")
else:
    print("No right to vote (not a citizen).")