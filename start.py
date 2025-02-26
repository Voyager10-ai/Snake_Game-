import turtle
import time
import random

# Game configuration
delay = 0.1
score = 0
high_score = 0

# Screen setup
wn = turtle.Screen()
wn.title("🐍 Snake Game - Pro Edition 🐍")
wn.bgcolor("#222831")  # Dark theme
wn.setup(width=700, height=700)
wn.tracer(0)  # Turns off automatic screen updates

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("#76ABAE")  # Cyan-blue
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("#F05454")  # Red
food.penup()
food.goto(0, 100)

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Score: 0  High Score: 0", align="center", font=("Arial", 24, "bold"))

# Snake body segments
segments = []

# Movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard controls
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()
    
    # Border collision
    if abs(head.xcor()) > 340 or abs(head.ycor()) > 340:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 24, "bold"))
    
    # Food collision
    if head.distance(food) < 20:
        x, y = random.randint(-300, 300), random.randint(-300, 300)
        food.goto(x, y)
        
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("#FFDE59")  # Gold tail
        new_segment.penup()
        segments.append(new_segment)
        
        delay -= 0.002
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 24, "bold"))
    
    # Move the segments
    for i in range(len(segments) - 1, 0, -1):
        x, y = segments[i - 1].pos()
        segments[i].goto(x, y)
    
    if segments:
        segments[0].goto(head.pos())
    
    move()
    
    # Check for body collision
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 24, "bold"))
    
    time.sleep(delay)

wn.mainloop()
