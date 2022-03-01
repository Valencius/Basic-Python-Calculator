choice = "0"
print("Welcome to 2 Number Calculator!")
while choice != "5":
    i = 0
    while i <= 10:
        print("")
        i += 1
    print("Welcome to 2 Number Calculator!")
    print("what would you like to do :")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input(">> ")
    if choice == "1":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        total = str(int(num1) + int(num2))
        print("Total = " + total)
        enter = input("Press enter to continue..")
    elif choice == "2":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        total = str(int(num1) - int(num2))
        print("Total = " + total)
        enter = input("Press enter to continue..")
    elif choice == "3":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        total = str(int(num1) * int(num2))
        print("Total = " * total)
        enter = input("Press enter to continue..")
    elif choice == "4":
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        total = str(int(num1) / int(num2))
        print("Total = " + total)
        enter = input("Press enter to continue..")
    elif choice == "5":
        choice = "5"
    else:
        choice = "0"

