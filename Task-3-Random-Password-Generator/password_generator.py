
import string
import secrets

print("===== RANDOM PASSWORD GENERATOR =====")

while True:
    try:
        length = int(input("Enter password length (minimum 8): "))
        if length < 8:
            print("Length must be at least 8.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

print("\nChoose character types:")
print("1. Lowercase letters")
print("2. Uppercase letters")
print("3. Numbers")
print("4. Symbols")

while True:
    choices = input("Enter choices (e.g. 1,2,3): ")
    choices = choices.replace(" ", "").split(",")

    if any(c not in ["1", "2", "3", "4"] for c in choices):
        print("Invalid choice. Try again.")
        continue

    choices = list(set(choices))

    if len(choices) < 2:
        print("Select at least two types.")
        continue
    break

characters = ""
groups = []

if "1" in choices:
    characters += string.ascii_lowercase
    groups.append(string.ascii_lowercase)

if "2" in choices:
    characters += string.ascii_uppercase
    groups.append(string.ascii_uppercase)

if "3" in choices:
    characters += string.digits
    groups.append(string.digits)

if "4" in choices:
    characters += string.punctuation
    groups.append(string.punctuation)

while True:
    password = [secrets.choice(group) for group in groups]

    for _ in range(length - len(password)):
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)
    print("\nGenerated password:", "".join(password))

    again = input("Generate another password? (yes/no): ").lower()

    if again != "yes":
        print("Thank you for using Password Generator!")
        break
