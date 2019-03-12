# A program that asks a user to input a series of positive numbers and displays
# the sum of the positive numbers. The program will terminate the series when
# the user inputs a negative number.
# 3-8-2019
# CTI-110-0003 P4HW3 - Sum of Numbers
# Clayton Zepeda
#

# set the accumulator to 0
# input = Prompt user to input a number positive number to start the sum process
# or enter a negative number to terminate the loop and display the sum.
# process = Calculate the sum of all positive numbers.
# output = Display sum of all positive numbers.



def main():    

# Prompt user for a number to start accumulation loop or a negative number to
# terminate the loop.
    print('Enter a positive number to add to a sum of numbers.')
    print('Enter a negative number to quit and display the total sum.')

# Set the accumulator value to 0.
    total = 0

# Create loop to continue until a negative number is entered. The loop will
# continue to add numbers to a total sum until a number entered is less than 0.
    number = float(input('Enter a number: '))
    while number > -1:
# process = Calculate the sum of all positive numbers.
        total = total + number
        print('\nEnter a positive number to continue ' \
              'or a negative number to quit.')
        number = float(input('Enter the next number: '))
       
# output = Display sum of all positive numbers.
    print('\nThe sum of all numbers is',format(total,".2f"))

main()
