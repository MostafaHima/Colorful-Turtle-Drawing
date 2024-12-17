import turtle as t
import random

# List of basic colors to choose from
colors = ["red", "lime", "black", "yellow", "medium violet red"]

# Create a turtle object
timy = t.Turtle()

# Set up the screen
window = t.Screen()
window.bgcolor("black")

# Set the colormode to use RGB values
t.colormode(255)

# Function to generate random RGB colors
def colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# Set the turtle speed to the fastest
timy.speed(0)

# Loop to draw multiple circles with random colors and rotated angles
for step in range(0, 361, 3):
    timy.color(colors())  # Change the color
    timy.circle(110)  # Draw a circle with radius 110
    timy.setheading(step)  # Set the turtle's heading to rotate by 3 degrees at each step

# Hide the turtle after drawing
timy.hideturtle()

# Keep the window open
window.mainloop()
