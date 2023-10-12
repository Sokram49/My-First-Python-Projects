''' Tech With Tim's Python Beginner Project Tutorial - Turtle Racing!
    I made it so that the turtles race from left to right
    I wanted to make a replay feature but it doesn't work '''

import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "green", "blue", "orange", "yellow", "black", "pink", "brown", "cyan", "purple"]

def get_racers():
    racers = 0
    while True:
        racers = input("Enter number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Enter a number.")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2-10.")        

def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if x >= WIDTH // 2 - 10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles = []
    spacingy = HEIGHT // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.penup()
        racer.setpos(-WIDTH//2 + 20, HEIGHT//2 - (i + 1) * spacingy)
        racer.pendown()
        turtles.append(racer)

    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")

while True:
    racers = get_racers()
    init_turtle()

    random.shuffle(COLORS)
    colors = COLORS[:racers]

    winner = race(colors)
    print(f"{winner} is the winning turtle!")
    turtle.bye()

    replay = input("Would you like to race the turtles again? (y/n): ").lower()
    if replay == "y":
        continue
    else:
        print("Thank you for racing!")
        break
