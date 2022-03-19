import turtle
tao = turtle.Pen()

def flower():
    for i in range(10):
        tao.circle(50)
        tao.left(36)

    tao.right(90)
    tao.forward(300)
flower()
def move(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()
    
tao.left(90)
move(100,0)
flower()
    
