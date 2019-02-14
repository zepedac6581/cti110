#Write a program that determines the areas of two rectangles and displays
#which area is the largest, or if they are equal.
#
#P3T1 - Areas of Rectangles
#Clayton Zepeda
#2-12-2019
#


#Input the length and width of rectangle_1.
length_1 = int(input('Enter the length of rectangle 1: '))
width_1 = int(input('Enter the width of rectangle 1: '))

#Input the length and width of rectangle_2.
length_2 = int(input('Enter the length of rectangle 2: '))
width_2 = int(input('Enter the width of rectangle 2: '))

#Calculate the area_1 of rectangle_1.
area_1 = length_1 * width_1
#Calculate the area_2 of rectangle_2.
area_2 = length_2 * width_2

#if area_1 > area_2
#   display "Rectangle 1 has the greatest area."
if area_1 > area_2:
    print("Rectangle 1 has the greatest area.")

#else if area_1 < area_2
    #   display "Rectangle 2 has the greatest area."
elif area_1 < area_2:
    print("Rectangle 2 has the greatest area.")

#else area_1 == area_2
#   display "Both rectangles have equal area."
elif area_1 == area_2:
    print("Both rectangles have equal area.")
