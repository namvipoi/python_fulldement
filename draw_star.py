from turtle import *
import turtle
#tạo đối tượng vẽ 
st = turtle.Turtle()
st.fillcolor("black")
st.begin_fill()
for i in range(5):
    st.forward(200)
    st.right(144)
st.end_fill()
turtle.done()