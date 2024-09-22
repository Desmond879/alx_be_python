# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter for the while loop
row = 0

# While loop to go through each row
while row < size:
    # For loop to print the asterisks for the current row
    for _ in range(size):
        print("*", end="")
    # Move to the next line after the row is printed
    print()
    
    # Increment the row counter
    row += 1
