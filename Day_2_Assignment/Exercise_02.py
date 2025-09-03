def main():
    items = []

    while True:
        user_input = input("Would you like to\n(1)Add or\n(2)Remove items or\n(3)Quit?: ")

        if user_input == "1":
            item = input("What will be added?: ")
            items.append(item)

        elif user_input == "2":
            if len(items) == 0:
                print("The list is empty, nothing to remove.")
                continue

            print(f"There are {len(items)} items in the list.")
            try:
                index = int(input("Which item is deleted?: "))
                if 0 <= index < len(items):
                    items.pop(index)
                else:
                    print("Incorrect selection.")
            except ValueError:
                print("Incorrect selection.")

        elif user_input == "3":
            print("The following items remain in the list:")
            for item in items:
                print(item)
            break

        else:
            print("Incorrect selection.")

main()