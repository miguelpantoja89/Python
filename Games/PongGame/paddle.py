import turtle
import winsound
window = turtle.Screen()

window.title("Pong Classic")
window.bgcolor("black")
window.setup(width=800, height= 600)
window.tracer(0)

score1 = 0
score2 = 0

# Paddle One

paddle1= turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup() # not draw the line
paddle1.goto(-350,0)

# Paddle Two

paddle2= turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350,0)
# Ball
ball= turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

ball.dx = -0.25
ball.dy = -0.25

#Pen
pen =turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player One: 0 Player Two: 0", align="center",font=("Courier",24,"normal"))
# Function Movements: 

def paddle1_up():
    y = paddle1.ycor()
    y +=20
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    y -=20
    paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    y +=20
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    y -=20
    paddle2.sety(y)
# keybord binding

window.listen()
window.onkeypress(paddle1_up,"w") # call function paddle1_up when key w is press
window.onkeypress(paddle1_down,"s")
window.onkeypress(paddle2_up,"Up")
window.onkeypress(paddle2_down,"Down")


while True:
    window.update()

    # Ball Move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball Bouncing
    if ball.ycor() >290:
        ball.sety(290)
        winsound.PlaySound("Pong Sound Effect.wav", winsound.SND_ASYNC)
        ball.dy *=-1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        winsound.PlaySound("Pong Sound Effect.wav", winsound.SND_ASYNC)
        ball.dy *=-1

    if ball.xcor() > 390 : 
        ball.goto(0,0)
        winsound.PlaySound("Pong Sound Effect.wav", winsound.SND_ASYNC)
        ball.dx *= -1
        score1 +=1
        pen.clear()
        pen.write("Player One: {} Player Two: {}".format(score1,score2), align="center",font=("Courier",24,"normal"))
    if ball.xcor() < -390 : 
        ball.goto(0,0)
        winsound.PlaySound("Pong Sound Effect.wav", winsound.SND_ASYNC)
        ball.dx *= -1
        score2 +=1
        pen.clear()
        pen.write("Player One: {} Player Two: {}".format(score1,score2), align="center",font=("Courier",24,"normal"))
    
    # Paddle and ball collisions

    if ball.xcor() > 340 and ball.xcor() <350 and (ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50):
        ball.setx(340)
        winsound.PlaySound("Pong Sound Effect.wav", winsound.SND_ASYNC)
        ball.dx *= -1
    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50):
        ball.setx(-340)
        winsound.PlaySound("Pong Sound Effect.wav", winsound.SND_ASYNC)
        ball.dx *= -1