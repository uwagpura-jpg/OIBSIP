while True:
    try:
        weight = float(input("Enter your weight = "))

        if weight <= 0:
            print("Weight must be greater than 0.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        height = float(input("Enter the height = "))

        if height <= 0:
            print("Height must be greater than 0.")
            continue

        break

    except ValueError:
        print("Please enter a valid number.")
BMI = weight / (height * height)

if BMI < 18.5:
    category = "Underweight"

elif BMI < 25:
    category = "Normal weight"

elif BMI < 30:
    category = "Overweight"

else:
    category = "Obese"

print("\n================================")
print("        BMI CALCULATOR")
print("================================")
print(f"Your BMI: {BMI:.2f}")
print(f"Category: {category}")
print("================================")


