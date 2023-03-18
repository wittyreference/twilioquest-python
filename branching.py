import sys

first_input = int(sys.argv[1])
second_input = int(sys.argv[2])
sum_to_use = first_input + second_input

if sum_to_use <= 0:
    print("You have chose the path of destitution.")
elif sum_to_use <= 100:
    print("You have chose the path of plenty.")
else:
    print("You have chose the path of excess.")