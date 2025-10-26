# pattern_drawing.py

# Ask the user for the size of the square pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Draw the square pattern
while row < size:
    for col in range(size):
        print("*", end="")
    print()  # Move to the next row
    row += 1
