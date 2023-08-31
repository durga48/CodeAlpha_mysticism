import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("pink")

# Create a turtle
t = turtle.Turtle()
t.speed(0)  # Set maximum drawing speed

# List of colors
colors = ["white", "gold", "blue", "purple", "green"]

# Draw mysticism-related design
for _ in range(72):
    t.color(colors[_ % len(colors)])
    t.pensize(10)
    t.forward(100)
    t.left(45)
    t.forward(50)
    t.left(45)
    t.forward(150)
    t.left(45)
    t.forward(50)
    t.left(45)
    t.forward(100)
    t.left(90)

# Hide the turtle
t.hideturtle()

# Keep the window open until it's closed by the user
turtle.mainloop()