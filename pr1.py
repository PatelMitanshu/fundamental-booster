from datetime import date



print("Welcome to the Interactive Personal Data Collector!")
print("This program collects basic personal details and shows Python fundamentals in action.\n")

name = input("Please enter your name: ").strip()
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
favourite_number = int(input("Please enter your favourite number: "))

current_year = date.today().year
birth_year = current_year - age

print("\nThank you! Here is the information we collected:\n")
print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(
		f"Favourite Number: {favourite_number} "
		f"(Type: {type(favourite_number)}, Memory Address: {id(favourite_number)})"
	)

print(
		f"\nYour birth year is approximately: {birth_year} "
		f"(based on your age of {age})"
	)
print("\nThank you for using the Personal Data Collector. Goodbye!")
	


