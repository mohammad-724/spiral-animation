import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rainbow Spiral")

# Set up the turtle pen
pen = turtle.Turtle()
pen.speed(0)  # Fastest speed

# List of colors for the rainbow effect
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

# Draw the spiral
for x in range(360):
    pen.pencolor(colors[x % 6])  # Cycle through colors
    pen.width(x / 100 + 1)       # Gradually thicken the line
    pen.forward(x)               # Move forward by an increasing distance
    pen.left(59)                 # Turn slightly less than 60 degrees for the twist

# Close the window when clicked
screen.exitonclick()
