# Fundamental Booster — Interactive Personal Data Collector

This small Python project demonstrates basic Python fundamentals by interactively collecting personal information from the user and displaying values, types, and memory addresses.

## Features
- Uses `input()` and `print()` for console interaction
- Demonstrates type casting (`int()`, `float()`) and arithmetic
- Shows variable `type()` and `id()` for each collected value
- Calculates an approximate birth year from the provided age

## Requirements
- Python 3.8 or newer

## Files
- `pr1.py` — main interactive script that collects and displays data

## Usage
Run the script from the project folder:

```bash
python pr1.py
```

Follow the prompts to enter your name, age, height (in meters), and favourite number.

## Example Console Interaction

Welcome to the Interactive Personal Data Collector!

Please enter your name: Alice
Please enter your age: 25
Please enter your height in meters: 1.68
Please enter your favourite number: 7

Thank you! Here is the information we collected:

Name: Alice (Type: <class 'str'>, Memory Address: 140703847239568)
Age: 25 (Type: <class 'int'>, Memory Address: 9793456)
Height: 1.68 (Type: <class 'float'>, Memory Address: 140703847253232)
Favourite Number: 7 (Type: <class 'int'>, Memory Address: 9793312)

Your birth year is approximately: 1998 (based on your age of 25)

Thank you for using the Personal Data Collector. Goodbye!

> Note: Memory addresses and exact formatting will vary between runs and Python implementations.

## Development
This project is intentionally minimal and educational. Feel free to extend it with validation, file output, or a GUI.
