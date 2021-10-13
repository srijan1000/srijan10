import turtle
import random

win = turtle.Screen()
win.bgcolor()
win.addshape("gold.gif")
win.addshape("diamond.gif")
win.addshape("danger.gif")
win.addshape("start.gif")
        
score_pen = turtle.Turtle()
score_pen.ht()
score_pen.speed(10000000000000000000000000000000000000000000000000)
score_pen.pu()
score_pen.goto(-300,280)

coin = turtle.Turtle()
score = 0
coin.ht()
coin.pu()
coin.speed(100000000000000000000000000000000000000000)
cs = random.randint(-300,300)
coin.goto(cs,300)
coin.shape("gold.gif")
coin.rt(90)
coin.st()

score = 0

start = False

sh = 1

sbutton = turtle.Turtle()
sbutton.speed(10000000000000000000000000000000000000000000000000)
sbutton.shape("start.gif")

def startf (x,y):
    global start
    start = True

sbutton.onclick(startf)

def collect(x,y):
    global score
    global sh
    global s
    score += 10
    s = random.randint(1,10)
    cs = random.randint(-300,300)
    coin.goto(cs,300)
    if sh == 2:
        score += 10
    if sh == 3:
        score -= 15
    sh = random.randint(1,3)
    if sh == 3:
        coin.shape("danger.gif")
    if sh == 1:
        coin.shape("gold.gif")
    if sh == 2:
        coin.shape("diamond.gif")
    score_pen.clear()
    score_pen.write(score, font = ("Courier", 25, "bold"))
            
s = random.randint(1,10)
coin.onclick(collect)

win.colormode(255)
rcolor = random.randint(0,255)
gcolor = random.randint(0,255)
bcolor = random.randint(0,255)
r = (rcolor)
g = (gcolor)
b = (bcolor)

while True:
    if start :
        sbutton.ht()
        coin.st()
        coin.fd(s)
        if coin.ycor()<= -300:
            if sh == 3:
                score += 5
            if sh == 1:
                 score -= 10
            if sh == 2:
                score -= 10
            score_pen.clear()
            score_pen.write(score, font = ("Courier", 25, "bold"))
            s = random.randint(1,10)
            cs = random.randint(-300,300)
            coin.goto(cs,300)
            sh = random.randint(1,2)
            if sh == 1:
                coin.shape("gold.gif")
            if sh == 2:
                coin.shape("diamond.gif")
    if not start:
        coin.ht()
        score_pen.clear()
    #rainbow bg and rainbow score
    if r >= 250:
        r -= 10
    if r <= 5:
        r += 10
    if g >= 250:
        g -= 10
    if g <= 5:
        g += 10
    if b >= 255:
        b -= 10
    if b <= 0:
        b += 10
    win.bgcolor(r,g,b)
    color = random.randint(1,6)
    if color == 1:
        r -= 10
    if color == 2:
        g -= 10
    if color == 3:
        b -= 10
    if color == 4:
        r += 10
    if color == 5:
        g += 10
    if color == 6:
        b += 10


