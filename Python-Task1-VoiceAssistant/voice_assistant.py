
import datetime

print("===== PYTHON VOICE ASSISTANT =====")
print("Type 'help' to see commands.")

while True:
    command = input("\nYou: ").strip().lower()

    if command == "hello" or command == "hi":
        print("Assistant: Hello! How can I help you?")

    elif command == "time":
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print("Assistant: Current time is", current_time)

    elif command == "date":
        current_date = datetime.date.today()
        print("Assistant: Today's date is", current_date)

    elif command == "help":
        print("Available commands:")
        print("hello - Greeting")
        print("time  - Current time")
        print("date  - Today's date")
        print("calc  - Simple calculation")
        print("exit  - Close assistant")

    elif command == "calc":
        try:
            first = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            second = float(input("Enter second number: "))

            if operator == "+":
                result = first + second
            elif operator == "-":
                result = first - second
            elif operator == "*":
                result = first * second
            elif operator == "/" and second != 0:
                result = first / second
            elif operator == "/":
                print("Assistant: Cannot divide by zero.")
                continue
            else:
                print("Assistant: Invalid operator.")
                continue

            print("Assistant: Result =", result)

        except ValueError:
            print("Assistant: Please enter valid numbers.")

    elif command == "exit":
        print("Assistant: Goodbye!")
        break

    else:
        print("Assistant: Unknown command. Type 'help'.")
