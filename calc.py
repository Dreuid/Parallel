def add(x, y):
    """Returns the sum of x and y."""
    return x + y


def main():
    print("--- Python Calculator ---")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    while True:
        # Get user choice
        choice = input("\nEnter choice (1/2/3/4) or 'q' to quit: ")

        # Check if user wants to quit
        if choice.lower() == 'q':
            print("Exiting calculator. Goodbye!")
            break

        # Check if choice is one of the four options
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                if result == "Error: Cannot divide by zero.":
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()