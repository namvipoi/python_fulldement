import turtle
def drec():

    rec = turtle.Turtle()

    d = int(input("nhập vào chiều dài của hình chữ nhật: d = "))
    r = int(input("Nhập vào chiều rộng của hình chữ nhật: r = "))
    for i in range(1,5,1):
        if i % 2 != 0:
            rec.forward(d)
            rec.left(90)
        elif i % 2 ==0:
            rec.forward(r)
            rec.left(90)
    turtle.done()

drec()
