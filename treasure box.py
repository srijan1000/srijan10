import turtle
import random
import winsound

try:
    win = turtle.Screen()
    win.addshape("gold.gif")
    win.addshape("diamond.gif")
    win.addshape("ballon.gif")
    
    score_pen = turtle.Turtle()
    score_pen.ht()
    score_pen.speed(10000000000000000000000000000000000000000000000000)
    score_pen.pu()
    score_pen.goto(-300,280)

    gold = turtle.Turtle()
    score = 0
    gold.ht()
    gold.pu()
    gold.speed(100000000000000000000000000000000000000000)
    cs = random.randint(-300,300)
    gold.goto(cs,300)
    gold.shape("gold.gif")
    gold.rt(90)
    gold.st()
    score = 0

    sh = 1

    def collect(x,y):
        global score
        global sh
        global s
        score += 10
        s = random.randint(1,10)
        cs = random.randint(-300,300)
        gold.goto(cs,300)
        if sh == 2:
            score += 10
        if sh == 3:
            score -= 5
        sh = random.randint(1,3)
        if sh == 3:
            gold.shape("ballon.gif")
        if sh == 1:
            gold.shape("gold.gif")
        if sh == 2:
            gold.shape("diamond.gif")
        score_pen.clear()
        score_pen.write(score, font = ("Courier", 25, "bold"))
        winsound.Beep(1000,60)
        
    s = random.randint(1,10)
    gold.onclick(collect)
    while True:
        gold.fd(s)
        if score >= 0:
            score_pen.pencolor("green")
        if score == 0:
            score_pen.pencolor("black")
        if score <= 0:
            score_pen.pencolor("red")
        if gold.ycor()<= -300:
            if sh == 3:
                score -= 5
                score_pen.clear()
            s = random.randint(1,10)
            cs = random.randint(-300,300)
            gold.goto(cs,300)
            if sh == 1:
                score_pen.clear()
                score -= 10
            if sh == 2:
                score -= 10
                score_pen.clear()
            sh = random.randint(1,3)
            if sh == 3:
                gold.shape("ballon.gif")
            if sh == 1:
                gold.shape("gold.gif")
            if sh == 2:
                gold.shape("diamond.gif")
                score_pen.clear()
            score_pen.write(score, font = ("Courier", 25, "bold"))
            winsound.Beep(2000,1000)
    win.mainloop()
except:
    None
