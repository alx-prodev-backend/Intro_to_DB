# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


try:
    degree = float(input("Enter the temperature to convert: "))
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")

choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if choice == "C":
    result = convert_to_fahrenheit(degree)
    print(f"{degree}°C is {result}°F")

elif choice == "F":
    result = convert_to_celsius(degree)
    print(f"{degree}°F is {result}°C")

else:
    print("Invalid unit. Please enter C or F.")
