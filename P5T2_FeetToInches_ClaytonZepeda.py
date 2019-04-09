# A program that will prompt the user for a number of feet, convert the number
# of feet to inches, and then display the results. 
# 3-19-2019
# CTI-110-0003 P5T2_FeetToInches_ClaytonZepeda
# Clayton Zepeda
#

# There are 12 inches in a foot.
# Prompt the user for a number of feet.
# Pass the input to a function.
# Convert the number of feet to inches.
# Display the results.

# define the conversion variables. 12 inches in 1 foot.
inches_per_foot = 12


def main():
    # Prompt user for input.
    feet = int(input('Enter the number of feet: '))

    # Convert the feet to inches.
    print(feet, 'feet equals', feet_to_inches(feet), 'inches')

# This function converts feet to inches.            
def feet_to_inches(feet):
    return feet * inches_per_foot

main()
