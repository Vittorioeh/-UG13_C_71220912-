import turtle 
s = turtle.Screen()
t = turtle.Turtle()
u = turtle.Turtle()

#setup
s.bgcolor('#FF69B4')
t.pensize(8)
u.pensize(8)

t.right(90)
t.forward(50)
t.right(90)
t.forward(20)
t.right(180)
t.forward(40)

t.right(90)
t.penup()
t.forward(60)
t.pencolor('#00008B')
t.pendown()
t.left(180)
t.circle(30,180)
t.penup()
t.circle(30,180)
t.left(180)
t.pendown()
t.right(40)
t.forward(95)
t.left(130)
t.forward(55)

t.penup()
t.goto(0,0)
t.forward(60)

t.pendown()
t.pencolor('#8B0000')
t.left(90)
t.forward(50)
t.left(180)
t.forward(100)
t.left(180)
t.forward(50)
t.right(90)
t.forward(60)
t.left(90)
t.forward(50)
t.left(180)
t.forward(100)

u.left(90)
u.forward(50)
u.left(135)
u.forward(25)
u.left(180)
u.forward(25)
u.left(45)

u.right(90)
u.penup()
u.forward(30)
u.left(90)
u.forward(115)
u.pendown()
u.pencolor('#FFFFFF')
u.circle(30)
u.right(180)
u.forward(60)
u.penup()
u.circle(-30,-180)
u.pendown()
u.circle(-30,-180)

u.penup()
u.goto(0,0)
u.right(90)
u.forward(90)
u.left(90)
u.forward(50)

u.pendown()
u.pencolor('#00FF00')
u.left(160)
u.forward(100)
u.left(180)
u.forward(100)
u.left(20)
u.right(160)
u.forward(100)

s.exitonclick()