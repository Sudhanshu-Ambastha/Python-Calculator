def calculator():
    result = None
    while True:
        if result is None:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue
        else:
            num1 = result
            try:
                num2 = float(input("Enter next number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

        choice = input("Choose operator (+, -, *, /) or 'c' to clear or 'q' to quit: ")

        if choice == "+":
            result = num1 + num2
            print("Result:", result)
        elif choice == "-":
            result = num1 - num2
            print("Result:", result)
        elif choice == "*":
            result = num1 * num2
            print("Result:", result)
        elif choice == "/":
            if num2 == 0:
                print("Cannot divide by zero.")
                continue
            result = num1 / num2
            print("Result:", result)
        elif choice == 'c':
            result = None
            print("Calculator cleared.")
        elif choice == 'q':
            print("Exiting calculator.")
            break
        else:
            print("Invalid choice. Please enter +, -, *, /, c, or q.")

calculator()
