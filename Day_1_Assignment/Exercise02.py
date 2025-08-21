age = int(input("What is your age? "))

if age >= 15 and age < 18:
    weight = float(input("What is your weight? "))
    if weight >= 55:
        print("Medicine can be used")
    else:
        print("Medicine cannot be used")
else:
    print("Medicine cannot be used")