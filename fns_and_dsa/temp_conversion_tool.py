# temp_conversion_tool.py

# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Function to prompt user and perform the temperature conversion
def main():
    try:
        # Prompt user for temperature
        temp = float(input("Enter the temperature to convert: "))
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Ask if the temperature is in Celsius or Fahrenheit
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Perform the conversion based on the unit
    if unit == 'F':
        celsius = convert_to_celsius(temp)
        print(f"{temp}°F is {celsius:.2f}°C")
    elif unit == 'C':
        fahrenheit = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {fahrenheit:.2f}°F")
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# Entry point of the script
if __name__ == "__main__":
    main()
