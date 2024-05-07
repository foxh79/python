numbers = [1, 2, 3, 4, 5, 6, 7, 14]

# Initialize the maximum number to the smallest possible value
max_number = numbers[0]

# Iterate over the list of numbers
for number in numbers:
    # If the current number is greater than the maximum number, update the
    # maximum number to the current number
    if number > max_number:
        max_number = number

# Print the maximum number
print(f"Maximum number is {max_number}")

#alternatively using the max() function
max_number = max(numbers)
print(f"Maximum number using math function is {max_number}")