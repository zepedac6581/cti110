# Write a turtle program that will draw my first and last
# initials.
# 3-5-2019
# CTI-110-0003 - Initials
# Clayton Zepeda
#

# import the turtle program window
def main():
    import turtle
    turtle.shape('turtle')

# Move turtle into position to write the first initial. This is done to allow
# more room to include both initials in a more centered position. 
    turtle.penup()
    turtle.left(180)
    turtle.forward(30)
    turtle.pendown()
# Use input or controlled loops input to write the first intitial 'C'.
    for x in range(0,10):
        turtle.forward(20)
        turtle.right(20)
# Move turtle into position to write the second initial
    turtle.penup()
    turtle.left(20)
    turtle.forward(75)
    turtle.pendown()
# Use input or controlled loops input to write the second initial 'Z'.
    turtle.forward(50)
    turtle.right(120)
    turtle.forward(130)
    turtle.left(120)
    turtle.forward(50)
    

    
main()
