# Maze Game
# ---------
# Author          : Phil Hall
#                   https://github.com/rhubarbdog
# First Published : April 2019

from microbit import *

MAZE = [ "wwwwwwwwwwwwwwwwwwwwwwwww" ,
         "w        w              w" ,
         "w        w              w" ,
         "w   wwwwwwwwwwww   wwwwww" ,
         "w   w  w       w   w    w" ,
         "w   w          w   w    w" ,
         "w   w      w   w   w    w" ,
         "w   w  w   w   w   w    w" ,
         "w   wwww   w   w   w    w" ,
         "w      w   w       w    w" ,
         "w   w  w   w       w    w" ,
         "w   wwww   wwwwwwwww    w" ,
         "w                       w" ,
         "w                       w" ,
         "wwwwwwwwwwwwwwwwwwwwwwwww" ]

DISPLAY = { "w" : 9 , 
            " " : 0 }

max_x=len(MAZE[0])
max_y=len(MAZE)
SCREEN=5
JOY_TOLLERANCE=250


player_x, player_y = (1, 12)
exit_x, exit_y = (20, 2)

loop = 0

while True:
    view_x = player_x - 2
    if view_x < 0:
        view_x = 0
    elif view_x > max_x - SCREEN:
        view_x = max_x - SCREEN

    view_y = min(max(player_y - 2, 0),max_y - SCREEN)

    for tmp_x in range(SCREEN):
        for tmp_y in range(SCREEN):
            display.set_pixel(tmp_x, tmp_y,\
                              DISPLAY[MAZE[view_y + tmp_y][view_x + tmp_x]])

    tmp_x = player_x - view_x
    tmp_y = player_y - view_y 
    if tmp_x in range(SCREEN) and tmp_y in range(SCREEN):
        if loop % 2:
            display.set_pixel(tmp_x, tmp_y, 5)
        else:
            display.set_pixel(tmp_x, tmp_y, 0)

    tmp_x = exit_x - view_x
    tmp_y = exit_y - view_y 
    if tmp_x in range(SCREEN) and tmp_y in range(SCREEN):
        if loop < 10:
            pix = loop
        else:
            pix = 19 - loop
        pix = max(1, pix)
        display.set_pixel(tmp_x, tmp_y, pix)

    if player_x == exit_x and player_y == exit_y:
        break
    
    joy_x=accelerometer.get_x()
    joy_y=accelerometer.get_y()

    if joy_y<-JOY_TOLLERANCE:
        delta_y=-1
    elif joy_y>JOY_TOLLERANCE:
        delta_y=1
    else:
        delta_y=0

    if joy_x<-JOY_TOLLERANCE:
        delta_x=-1
    elif joy_x>JOY_TOLLERANCE:
        delta_x=1
    else:
        delta_x=0

    if delta_x != 0 and delta_y != 0:
        if abs(joy_x) > abs(joy_y):
            delta_y = 0
        else:
            delta_x = 0

    if loop % 5 == 0:
        tmp_x = player_x + delta_x
        tmp_y = player_y + delta_y

        if tmp_x in range(max_x) and tmp_y in range(max_y) and\
           MAZE[tmp_y][tmp_x] == ' ':
            player_x = tmp_x
            player_y = tmp_y

    sleep(100)
    loop += 1
    loop %= 20

display.clear()
sleep(500)
display.scroll('Well done.')
