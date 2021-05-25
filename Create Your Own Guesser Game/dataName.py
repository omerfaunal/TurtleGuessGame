"""
    File name: dataName.py
    Author: Ömer Ünal
    Date created: 25/05/2021
    Python Version: 3.9

"""

from turtle import Turtle
import random
# You can customize font
FONT = ("Comic Sans MS", 6, "normal")
COLORS = ["blue", "orange", "red", "purple", "black", "pink", "coral", "DarkCyan", "CadetBlue", "DarkGreen"]


class DataName(Turtle):
    # This class creates a turtle and sends it to the given coordinates.
    def __init__(self, x, y, state_name):
        super().__init__()
        color = random.choice(COLORS)
        self.hideturtle()
        self.penup()
        self.color(color)
        self.goto(int(x), int(y))
        self.write(state_name, align="center", font=FONT)
