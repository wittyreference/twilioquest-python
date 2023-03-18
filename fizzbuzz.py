import sys

# Assign command line arguments to the variable "list_of_numbers"
list_of_numbers = sys.argv

# Remove the first element of the list (which is the name of the script being executed)
list_of_numbers.pop(0)

# Iterate through each number in the "list_of_numbers" variable
for number in list_of_numbers:
    # Convert the current number to an integer and assign to the variable "x"
    x = int(number)
    # Check if "x" is divisible by 3 and 5
    if x%3 == 0 and x%5 == 0:
        print('fizzbuzz')
    # Check if "x" is divisible by 3
    elif x%3 == 0:
        print('fizz')
    # Check if "x" is divisible by 5
    elif x%5 == 0:
        print('buzz')
    else:
        print(x)
        pass
