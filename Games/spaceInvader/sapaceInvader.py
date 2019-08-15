import turtle 
import os
import math
import random
import winsound

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invader")
wn.bgpic("back.gif")

#Register Shapes



wn.addshape("spacin.gif")


border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)

area = turtle.Turtle()
area.speed(0)
area.color("red")
area.penup()
area.setposition(-300, 100)
area.pendown()
area.pensize(3)


for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

for side in range(1):
    area.fd(600)
    area.lt(90)
area.hideturtle()

score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.penup()
score_pen.color("white")
score_pen.setposition(-290,275)
scorestring = "Score : %s" %score
score_pen.write(scorestring, False , align="left", font=("Arial", 14, "normal") )
score_pen.hideturtle()

name = turtle.Turtle()
name.speed(0)
name.penup()
name.color("yellow")
name.setposition(0,310)
scorestring2 = "SPACE INVADERS"
name.write(scorestring2, False , align="center", font=("Arial", 19, "normal") )
name.hideturtle()

# Player creation
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playspeed = 15




# Choose number of enemies
number_enemies= 5
enemies = []


# Add enemies to list
for i in range(number_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    # Enemy Creation:

    
    enemy.color("green")
    enemy.shape("spacin.gif")
    enemy.penup()
    enemy.speed(0)
    x =random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x,y)

enemyspeed = 3




# Bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("square")
bullet.penup()
bullet.setheading(90)
bullet.speed(0)
bullet.shapesize(stretch_wid=0.19, stretch_len=0.4)
bullet.hideturtle()

bulletspeed = 20

# Bullet state
# ready - ready to fire
# fire - bullet is firing
bulletstate = "ready"

# Player moves:
def move_left():
    x = player.xcor()
    x -=playspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    # Declare global for change it
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        # move bullet just above  the player
        x = player.xcor()
        y = player.ycor() + 20
        bullet.setposition(x ,y)
        bullet.showturtle()

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else: 
        return False

def create_invader():
    enemy = turtle.Turtle()
    global enemies
    enemy.color("green")
    enemy.shape("spacin.gif")
    enemy.penup()
    enemy.speed(0)
    x =random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x,y)
    enemies.append(enemy)

wn.listen()
wn.onkeypress(move_left,"a")
wn.onkeypress(move_right,"d")
wn.onkeypress(fire_bullet,"space")


winsound.PlaySound("Space invaders remix-[AudioTrimmer.com].wav", winsound.SND_ASYNC + winsound.SND_LOOP)
while True:
    wn.update()
    

    for enemy in enemies:
        # Move the enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)
        #Game over
        if isCollision(player,enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break 

        if enemy.ycor() < -280:
            player.hideturtle()
            enemy.hideturtle()
            print("Game Over")
            break

        # Move enemy back and down:
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
        if enemy.xcor() < -280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *=-1
        # Bullet and enemy check collision

        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0,-400)

            # Update score
            score_pen.clear()
            score +=1
            scorestring = "Score : %s" %score
            score_pen.write(scorestring, False , align="left", font=("Arial", 14, "normal") )

            
            # Increase enemies

            create_invader()
            
            

            



            #Reset the enemy
            x =random.randint(-200,200)
            y = random.randint(100,150)
            enemy.setposition(x,y)

        
    # Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    # Border Bullet checking
    if bullet.ycor() > 275 :
        bullet.hideturtle()
        bulletstate = "ready"
    
    