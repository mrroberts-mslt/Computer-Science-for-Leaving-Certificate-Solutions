import turtle
#s = turtle.getscreen()
t = turtle.Turtle()
t.shape("turtle")
for i in range(4):
  t.fd(100)
  t.rt(90)
t.clear()




t.speed(0)
t.color("#FF0000")

side=20
t.penup()
t.goto(0,0) #position cursor at the bootom right of the screen
t.pendown()

for i in range (1,50):
  t.forward(side)
  t.left(92)
  side=side+7


t.penup()
t.goto(500,500)
