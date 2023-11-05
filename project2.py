
import turtle

window = turtle.Screen()
window.setup(800,500)
pen = turtle.Turtle()


window.bgcolor("light blue")
pen.speed(1)




def draw_rectangle(pen,length,width):
    pen.up()
    pen.goto(-400,-150)
    pen.down()
    pen.color("medium blue")
    pen.begin_fill()


    for _i in range(2):
        pen.forward(length)
        pen.right(90)
        pen.forward(width)
        pen.right(90)
    pen.end_fill()   
draw_rectangle(pen,800,100)


# boat 

pen.up()
pen.goto(-200,-80)
pen.down()
pen.color("saddlebrown")
pen.begin_fill()
pen.right(45)
pen.forward(100)
pen.left(45)
pen.forward(150)
pen.left(45)
pen.forward(100)
pen.left(135)
pen.forward(300)
pen.end_fill()



# mast
pen.up()
pen.goto(0, -80)
pen.down()
pen.color("black")
pen.begin_fill()
pen.right(90)
for _i in range(2):
    pen.forward(200)
    pen.left(90)
    pen.forward(10)
    pen.left(90)
pen.end_fill()


# right sail
pen.up()
pen.goto(0,120)
pen.down()
pen.color("white")
pen.begin_fill()
pen.right(130)
pen.forward(250)
pen.right(140)
pen.forward(190)
pen.end_fill()

#left sail
pen.up()
pen.forward(14)
pen.down()
pen.begin_fill()
pen.forward(180)
pen.right(139)
pen.forward(240)
pen.end_fill()

# sun
pen.up()
pen.goto(-300,150)
pen.down()
pen.color("yellow")
pen.begin_fill()
pen.circle(40)
pen.end_fill()




turtle.done()


pen.hideturtle()