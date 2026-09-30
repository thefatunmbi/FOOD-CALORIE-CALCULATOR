# Nigerian Food Calorie Calculator

A simple Python program that estimates the calories in common Nigerian foods based on the amount entered in grams.

This project was built as a **CS50P Week 0 mini-project** to practice Python fundamentals such as variables, user input, conditionals, functions, arithmetic, and return values.

## Features

* Accepts a food name from the user
* Accepts the food's weight in grams
* Looks up the estimated calories per 100g
* Calculates the estimated total calories
* Handles foods that are not included in the calculator

## Foods Included

The current version includes:

* Rice
* Yam
* Potato
* Plantain
* Egg
* Chicken
* Beans
* Garri
* Bread
* Beef

## How It Works

The calculator uses the following formula:

```text
Total Calories = (Calories per 100g ÷ 100) × Weight in grams
```

For example, if rice is estimated at **123 kcal per 100g** and the user enters **300g**:

```text
(123 ÷ 100) × 300 = 369 kcal
```

The result is an estimate based on the calorie values used in the program.

## Example

```text
-----------Food calorie calculator-----------
Enter a food and its weight to calculate calories

Food: rice
Weight(g): 300

Food: rice
Weight: 300.0
Total calories 369.0
```

## How to Run

Make sure Python 3 is installed.

Clone the repository:

```bash
git clone <your-repository-url>
```

Move into the project directory:

```bash
cd nigerian-food-calorie-calculator
```

Run the program:

```bash
python3 calorie_calculator.py
```

## What I Learned

This project helped me practice:

* Defining and calling functions
* Passing arguments to functions
* Returning values from functions
* Using `if`, `elif`, and `else`
* Taking user input with `input()`
* Converting strings to numbers with `float()`
* Performing calculations with variables
* Handling invalid food input with `None`
* Organizing a small Python program

## Future Improvements

As I learn more Python, I plan to improve the project by adding:

* Better input validation
* More Nigerian foods
* More accurate and consistent nutritional data
* Support for multiple foods in one meal
* Daily calorie tracking
* Saving food records
* A database
* Eventually, a web version

## Project Background

This project is part of my journey through **Harvard's CS50P — Introduction to Programming with Python**.

The goal was not to build a perfect calorie-tracking application, but to use the Python concepts I had learned to build something useful and personal.

---

**Built with Python**
