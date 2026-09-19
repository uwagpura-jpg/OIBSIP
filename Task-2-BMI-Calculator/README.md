# BMI Calculator

A simple command-line BMI Calculator built using Python as part of my Oasis Infobyte Python Programming Internship.

## Features

- Takes weight and height as user input
- Calculates Body Mass Index (BMI)
- Handles invalid numeric input
- Rejects zero and negative weight or height values
- Displays BMI up to 2 decimal places
- Displays the BMI category

## Technologies Used

- Python 3
- Python built-in functions and control statements
- Loops
- Exception handling

## How It Works

The program takes the user's weight in kilograms and height in meters and calculates BMI using:

```text
BMI = Weight / (Height × Height)
```

The calculated BMI is then used to display the corresponding category.

## Input Validation

The program handles invalid input using Python's `try-except` exception handling.

It also checks that:

- Weight must be greater than 0
- Height must be greater than 0

If an invalid value is entered, the program asks the user to enter it again.

## How to Run

Make sure Python 3 is installed.

Open the project directory:

```bash
cd OIBSIP/Task-2-BMI-Calculator
```

Run the program:

```bash
python3 bmi_calculator.py
```

## Example

```text
Enter your weight = 45
Enter the height = 1.2

================================
        BMI CALCULATOR
================================
Your BMI: 31.25
Category: Obese
================================
```

## What I Learned

While building this project, I practiced:

- Taking input using `input()`
- Converting input using `float()`
- Variables and arithmetic operations
- `if`, `elif`, and `else`
- `while` loops
- `try-except` exception handling
- `break` and `continue`
- f-strings for formatted output
- Basic input validation
- Creating and documenting a Python project

## Project Structure

```text
Task-2-BMI-Calculator/
│
├── bmi_calculator.py
└── README.md
```

## Internship

This project was created as part of the **Oasis Infobyte Python Programming Internship (OIBSIP)**.

## Author

**Ummul Bani Wagpura**
