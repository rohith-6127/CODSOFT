import math

# ---------- Colors ----------
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

history = []

# ---------- Functions ----------

def show_menu():
    print(CYAN)
    print("=" * 45)
    print("      ADVANCED PYTHON CALCULATOR")
    print("=" * 45)
    print(RESET)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (x^y)")
    print("7. Square Root")
    print("8. Percentage")
    print("9. View History")
    print("10. Clear History")
    print("11. Exit")


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print(RED + "Invalid input! Please enter a valid number." + RESET)


while True:

    show_menu()

    choice = input("\nEnter your choice (1-11): ")

    if choice in ['1', '2', '3', '4', '5', '6', '8']:

        num1 = get_number("Enter First Number : ")
        num2 = get_number("Enter Second Number: ")

        if choice == '1':
            result = num1 + num2
            operation = f"{num1} + {num2} = {result}"

        elif choice == '2':
            result = num1 - num2
            operation = f"{num1} - {num2} = {result}"

        elif choice == '3':
            result = num1 * num2
            operation = f"{num1} × {num2} = {result}"

        elif choice == '4':
            if num2 == 0:
                print(RED + "Cannot divide by zero!" + RESET)
                continue
            result = num1 / num2
            operation = f"{num1} ÷ {num2} = {result}"

        elif choice == '5':
            result = num1 % num2
            operation = f"{num1} % {num2} = {result}"

        elif choice == '6':
            result = num1 ** num2
            operation = f"{num1}^{num2} = {result}"

        elif choice == '8':
            result = (num1 / num2) * 100
            operation = f"({num1}/{num2}) × 100 = {result}%"

        print(GREEN + "\nResult:", operation + RESET)
        history.append(operation)

    elif choice == '7':

        num = get_number("Enter Number: ")

        if num < 0:
            print(RED + "Square root of a negative number is not possible." + RESET)
            continue

        result = math.sqrt(num)
        operation = f"√{num} = {result}"

        print(GREEN + "\nResult:", operation + RESET)
        history.append(operation)

    elif choice == '9':

        print(BLUE + "\n========= CALCULATION HISTORY =========" + RESET)

        if history:
            for i, item in enumerate(history, start=1):
                print(f"{i}. {item}")
        else:
            print("No history available.")

        print("=" * 40)

    elif choice == '10':

        history.clear()
        print(YELLOW + "Calculation history cleared successfully!" + RESET)

    elif choice == '11':

        print(GREEN + "\nThank you for using Advanced Python Calculator!" + RESET)
        break

    else:
        print(RED + "Invalid choice! Please try again." + RESET)
