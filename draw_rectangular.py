import turtle
def drec(d, r):

    rec = turtle.Turtle()
    rec.left(90)
    rec.color("red")
    print(type(rec.color()))
    # p = rec.color()

    rec.begin_fill()
    for i in range(1,5,1):
        if i % 2 != 0:
            rec.forward(d)
            rec.right(90)
        elif i % 2 ==0:
            rec.forward(r)
            rec.right(90)
    rec.end_fill()
    turtle.done()

drec(100,90)


