import turtle

def draw_square(turtle):
    for i in range(0, 4):
        turtle.forward(100)
        turtle.right(90)
def art():
    window = turtle.Screen()
    window.bgcolor("green")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(100)

    angle = 0

    while angle < 360:
        draw_square(brad)
        brad.right(10)
        angle += 10



    # angie = turtle.Turtle()
    # angie.shape("arrow")
    # angie.color("red")
    # angie.circle(100)
    #
    # katoun = turtle.Turtle()
    # katoun.shape("circle")
    # katoun.color("pink")
    #
    # for i in range (0, 3):
    #     katoun.right(120)
    #     katoun.forward(50)

    window.exitonclick()

art()