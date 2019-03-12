# Write a program that will display the amount of calories burned during a
# number of minutes(20, 35, and 45). 
# 3-7-2019
# CTI-110-0003 P4HW1 - Calories Burned
# Clayton Zepeda
#

# 1 minute on a treadmill will burn 5 calories.
# Program calculates the number of calories burned for a number of minutes
# Displays the number of calories burned.



# 1 minute on treadmill = 5 calories burnt
calories = 5

def main():

# Create a range for the number of minutes to display increments of five
    for minutes in range(20, 46, 5):

# Program calculates the number of calories burned for a number of minutes by
# dividing minutes by 1, then multiplying minutes by calories.
        calories_burnt = ( minutes / 1)*calories

# Display the number of calories burnt.
        print(minutes,'minutes on a treadmill will burn',calories_burnt,\
              'calories.')

main()
