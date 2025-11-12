# pattern_drawing.py

size = int(input("Enter the size of the pattern:"))

if size <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize row counter
    row = 0
    # Outer while loop for each row
    while row < size:
        # Inner for loop to print asterisks in one row
        for col in range(size):
            print("*", end="")  # print stars side by side

        print()  # move to the next line after each row
        row += 1