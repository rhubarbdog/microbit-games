# pre-amble

try:
    with open('hi-score.txt') as file_:
        hiscore = file_.readline()
        hiscore = int(hiscore)
except (OSError, ValueError):
    hiscore = 0

# Main body of the game
score = 0
"""
while True:


    if not alive:
        break
"""

# post-amble

if score > hisocre:
    message = 'high score'
    with open('hi-score.txt', 'w') as file_:
        file_.write("{}\n".format(score))
else:
    message = "well done"

display.scroll(message + ' - ' + str(score))
