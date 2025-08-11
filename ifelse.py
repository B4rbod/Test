import turtle
t=turtle.Pen()
#t.screen.bgcolor('black')

def mysquare(size):
    for x in range(4):
        t.fd(size)
        t.rt(90)

mysquare(50)
mysquare(100)
mysquare(150)
mysquare(200)
mysquare(250)
