'''
AUTHOR: endlessutopia7
DATE: 2022/07/06
A draw app
'''

from time import *
from random import *

# unit: second
SLEEP_INTERVAL = 5

def draw():
    drawPool = []
    itemCount = int(input("Number of items: "))
    for i in range(itemCount):
        elementHint = "Item %d: " % (i + 1)
        nextElement = input(elementHint)
        drawPool.append(nextElement)

    drawCount = int(input("Number of draws: "))
    drawCount = min(drawCount, itemCount)
    for i in range(drawCount):
        drawHint = "Drawed element %d: " % (i + 1)

        candidate = choice(drawPool)
        print(drawHint + candidate)
        drawPool.remove(candidate)

        # simulate sleep time
        if i < drawCount - 1:
            sleep(SLEEP_INTERVAL)

if __name__ == '__main__':
    draw()