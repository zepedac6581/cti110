# A turtle program that when executed, will draw a square and
# a triangle. 
# 3-5-2019
# CTI-110-0003 P4T1a - Shapes
# Clayton Zepeda
#

def main():
    import turtle
# Use the 'for' controlled loop to create a square shape.
    turtle.shape('turtle')
    for x in range(0,4):
        turtle.forward(100)
        turtle.left(90)
# Move turtle away from the square to begin drawing another shape.
    turtle.penup()
    turtle.right(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.pendown()
# Use the 'for' controlled loop to draw a triangle. 
    turtle.color('green')
    turtle.pensize(5)
    for x in range(0,3):
        turtle.forward(150)
        turtle.left(120)

main()
