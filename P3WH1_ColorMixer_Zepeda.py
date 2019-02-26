# A program that allows users to input primary colors as a mix and ouputs
# a secondary color.
# CTI-110-0003
# P3HW1 - Color Mixer
# Clayton Zepeda 
# 2-14-2019
#

def main():
# User inputs two primary colors
# Primary colors are red, blue and yellow.
     print("The primary colors are red, blue, and yellow.")
     primary_color_1 = input('Enter the first primary color to mix: ')
     primary_color_2 = input('Enter the second primary color to mix: ')
     
# if Mixing primary_1 == red and primary_2 == blue:
#   print('The secondary color is purple.')
     if (primary_color_1 in ("red","Blue","blue","Red")and primary_color_2 in\
         ("blue","red","Red","Blue")):
         print("The secondary color is purple.")
     
# if else Mixing primary_1 == red and primary_2 == yellow
#    print('The secondary color is orange.')
     elif (primary_color_1 in("red","Red","Yellow","yellow") and primary_color_2 in\
           ("yellow","Yellow","Red","red")):
             print("The secondary color is orange.")

# if else Mixing primary_1 == blue and primary_2 == yellow
#    print('The secondary color is green.')
     elif (primary_color_1 in ("blue","Blue","Yellow","yellow") and primary_color_2 in\
           ("yellow","Yellow","Blue","blue")):
             print("The secondary color is green.")
        
# if user inputs a primary color not equal to primary_1, primary_2 or primary_3
#   display 'Error; input color is not a primary.'
     else:
         print("Error! One color entered is not a primary color.")
main()
