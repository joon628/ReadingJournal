import turtle

#------------------------------------------------------------------------------
# Starter code to get things going
# (feel free to delete once you've written your own functions
#------------------------------------------------------------------------------

# Create the world, and a turtle to put in it
bob = turtle.Turtle()

# Get moving, turtle!
bob.fd(100)

# Wait for the user to close the window
turtle.mainloop()


#------------------------------------------------------------------------------
# Make some shapes
#   Work through exercises 1-4 in Chapter 4.3.
#------------------------------------------------------------------------------

# NOTE: for part 2 of 4.3, you will add another parameter to this function
def square(t):
    t = turtle.Turtle()
    for i in range(t):
        t.forward(100) #Assuming the side of a pentagon is 100 units
        t.right(90)


## Polygon
def polygon(t):
    #Python programming to draw pentagon in turtle programming
    t = turtle.Turtle()
    for i in range(t):
        t.forward(100) #Assuming the side of a pentagon is 100 units
        t.right(360/t)

## Circle
def circle(t):
    t = turtle.Turtle()
    t.circle(60)


#------------------------------------------------------------------------------
# Make some art
#   Complete *at least one of* Exercise 2, 3, 4, or 5 in `shapes.py`.
#------------------------------------------------------------------------------

# If you come up with some cool drawings you'd like to share with the rest of the class, let us know!
def art(t):
    t = turtle.Turtle()

    for i in range(t):
        t.forward(100)
        t.right(3)
        t.forward(20)
        t.rotate(40)
        t.farward(30)
