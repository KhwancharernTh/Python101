import turtle

#3

colors = ['red','purple','blue','green','orange','yellow']
tao = turtle.Pen()
tao.shape('turtle')
tao.speed(2000)

turtle.bgcolor('black')

for i in range(360):
    tao.pencolor(colors[i%6])
    tao.width(i//100 + 1)
    tao.forward(i)
    tao.left(59)

turtle.done()

