# A program that will display a table of weights 100-300 in both pounds and
# kilograms.
# 3-8-2019
# CTI-110-0003 P4HW2 - Pounds to Kilos Table
# Clayton Zepeda
#

# 1lb = 2.2046kg
# Calculate conversion for every 10 pound step = (pound / 1)*2.2046
# Display the weights in a readable format.

# define the value of kg for conversion
kg = 2.2046

def main():

# Calculate conversion for every 10 pound step = (pound / 1)*2.2046
    for pounds in range(100, 301, 10):
        kilograms = (pounds / 1)*kg

# Display the weights and format display to 2nd decimal point.
        print(pounds,'pounds are equal to',format(kilograms, '.2f'),\
        'kilograms.')

        
main()
