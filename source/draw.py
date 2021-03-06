import pygame
import graphics
import game
import math
from sprite import Sprite

# Seconds in an in-game day / night cycle
# The ten seconds situation is merely for testing, we can make it longer later.
daySeconds = 1

# Maximum R, G, B values for sky color
_R = 164.0
_G = 240.0
_B = 238.0

# Minimum R, G, B value for sky color
_M = 13.0

# Maximum darkness for ambient; 0-255, 255 is darkest
maxDark = 186.0

# Minimum darkness for ambient
minDark = 0.0

colorList = [
    (_R + _M) / 2,
    (_G + _M) / 2,
    (_B + _M) / 2,
    False,  # True if the colors are darkening
    (maxDark + minDark) / 2
]


def rangec(num, minimum, maximum):
    n = num
    if n >= maximum:
        n = maximum
    elif n <= minimum:
        n = minimum
    return n


def solveColors(fr, delayed):
    notReallyGlobalVariableHi = (
        daySeconds) / ((1.0) * (delayed / fr)) / (fr / 1000)
    if not colorList[3]:
        colorList[0] += (_R - _M) / notReallyGlobalVariableHi
        colorList[1] += (_G - _M) / notReallyGlobalVariableHi
        colorList[2] += (_B - _M) / notReallyGlobalVariableHi
        colorList[4] -= (maxDark - minDark) / notReallyGlobalVariableHi
    else:
        colorList[0] -= (_R - _M) / notReallyGlobalVariableHi
        colorList[1] -= (_G - _M) / notReallyGlobalVariableHi
        colorList[2] -= (_B - _M) / notReallyGlobalVariableHi
        colorList[4] += (maxDark - minDark) / notReallyGlobalVariableHi

    if (colorList[0] >= _R and colorList[1] >= _G and colorList[2] >= _B and not colorList[3] and colorList[4] <= minDark) or (colorList[0] <= _M and colorList[1] <= _M and colorList[2] <= _M and colorList[3] and colorList[4] >= maxDark):
        if colorList[3]:
            colorList[3] = False
        else:
            colorList[3] = True

    colorList[0] = rangec(colorList[0], _M, _R)
    colorList[1] = rangec(colorList[1], _M, _G)
    colorList[2] = rangec(colorList[2], _M, _B)
    colorList[4] = rangec(colorList[4], minDark, maxDark)

    return (
        int((math.floor(colorList[0]), math.ceil(colorList[0]))[
            colorList[0] <= _R / 2]),
        int((math.floor(colorList[1]), math.ceil(colorList[1]))[
            colorList[1] <= _G / 2]),
        int((math.floor(colorList[2]), math.ceil(colorList[2]))[
            colorList[2] <= _B / 2])
    )


def draw_hud():
    """
    This is seperate mearly for simplicity
    """

    graphics.draw_text("Score: " + str(game.score), (14, 14, 14), (25, 25))


def draw(fr, delayed):
    """
    Drawing logic
    """

    # Draw background
    # color_overlay = solveColors(float(fr), float(delayed))
    # game.screen.fill(color_overlay)
    game.screen.fill((_R, _G, _B))

    game.world.draw()
    
    game.alvey.draw()

    game.test_map.draw()
    draw_hud()

    return