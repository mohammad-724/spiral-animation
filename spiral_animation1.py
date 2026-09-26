import turtle
import colorsys

# Screen setup
screen = turtle.Screen()
screen.setup(width=900, height=700)
screen.bgcolor("black")
screen.title("Animated Rainbow Spiral")

# Turtle setup
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

length = 1
angle = 15
hue = 0

def animate():
    global length, angle, hue

    # Generate rainbow color
    rgb = colorsys.hsv_to_rgb(hue, 1, 1)
    t.pencolor(rgb)

    # Draw one section of the spiral
    t.forward(length)
    t.right(angle)

    # Gradually expand the spiral
    length += 0.5

    # Change color gradually
    hue += 0.005
    if hue >= 1:
        hue = 0

    # Continue animation
    screen.ontimer(animate, 10)

# Start animation
animate()

# Keep the window open
screen.mainloop()
