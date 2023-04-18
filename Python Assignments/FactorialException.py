import sys

try:
    # Get number from command line argument
    number = int(sys.argv[1])

    # Check if number is negative
    if number < 0:
        print("Error: Number cannot be negative.")
    else:
        # Calculate factorial
        factorial = 1
        for i in range(1, number+1):
            factorial *= i
        print(f"The factorial of {number} is {factorial}")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")
except IndexError:
    print("Error: Number not provided. Please enter a number as a command line argument.")
