# A program that prompts a user to enter a distance in kilometers then converts
# the distance to miles and displays the results. 
# 3-19-2019
# CTI-110-0003 P5T1_KilometerConverter_ClaytonZepeda
# Clayton Zepeda
#

# The conversion formula is miles = milometers x 0.6214
# Prompt the user to input a distance in kilometers.
# Program will use the conversion formula to convert the distance to miles.
# Program will display the converted distance.

conversion = 0.6214

def main():
    # Prompt the user for the kilometers input.
    kilometers = float(input('Enter a distance in kilometers: '))

    # Pass the argument to show_miles, and display the results.
    show_miles(kilometers)
    
def show_miles(km):
    # Calculate the conversion.
    miles = km * conversion

    # Display the conversion results.
    print(km, 'kilometers equals', format(miles, ',.2f'), 'miles.')

main()
    
