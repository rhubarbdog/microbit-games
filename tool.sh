#!/bin/bash

uflash maze.py .
mv micropython.hex microbit-maze.hex
uflash snake.py .
mv micropython.hex microbit-snake.hex

git add microbit-maze.hex
git add microbit-snake.hex
