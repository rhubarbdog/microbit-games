# snake
# -----
# Author          : Phil Hall
#                   https://github.com/rhubarbdog

# License         : Creative Commons 4.0
# First Published : May 2019

from microbit import *
import random

JOY_TOLLERANCE = 250
SCREEN = 5

head_x = 2
head_y = 2
dx = 1
dy = 0

tail = []

food_x = None
food_y = None
score = 0

while True:
    display.clear()
    for t in tail:
        x,y = t
        display.set_pixel(x, y, 2)
    if (not food_x is None) and (not food_y is None):
        display.set_pixel(food_x, food_y, 9)
    display.set_pixel(head_x, head_y, 5)
    sleep(300)

    save_dx = dx
    save_dy = dy
    joy_x = accelerometer.get_x()
    joy_y = accelerometer.get_y()

    if joy_y < -JOY_TOLLERANCE:
        dy=-1
    elif joy_y > JOY_TOLLERANCE:
        dy=1

    if joy_x < -JOY_TOLLERANCE:
        dx=-1
    elif joy_x > JOY_TOLLERANCE:
        dx=1

    if dx != 0 and dy != 0:
        if abs(joy_x) > abs(joy_y):
            dy = 0
        else:
            dx = 0

    # Game Over? has the head bitten the tail?
    if len(tail) >= 1:
        if (abs(save_dx) == abs(dx) and save_dx != dx) or \
           (abs(save_dy) == abs(dy) and save_dy != dy):
            break

    break2 = False
    for t in tail:
        x,y = t
        if head_x == x and head_y == y:
            break2 = True
            break

    if break2:
        break

    # save the current head in the tail
    tail.append((head_x, head_y))

    # movement and wrap round
    head_x += dx
    head_y += dy

    if head_x < 0:
        head_x = SCREEN - 1
    if head_x >= SCREEN:
        head_x = 0

    if head_y < 0:
        head_y = SCREEN - 1
    if head_y >= SCREEN:
        head_y = 0

    # Place a food item if there is None
    if food_x is None and food_y is None:
        coin_flip = random.randrange(2)
        if coin_flip == 0:
            while food_x is None or food_y is None:
                food_x = random.randrange(SCREEN)
                food_y = random.randrange(SCREEN)
                if food_x == head_x and food_y == head_y:
                    food_x = None
                    food_y = None
                else:
                    for t in tail:
                        x,y = t
                        if food_x == x and food_y == y:
                            food_x = None
                            food_y = None
                            break

    # if no food 'forget' the saved place else 'eat it'
    if not (head_x == food_x and head_y == food_y):
        tail.pop(0)
    else:
        food_x = None
        food_y = None
        score += 1

display.scroll( "Game Over - " + str(score), wait = False, loop = True)
