"""
    File name: countryeName.py
    Author: Ömer Ünal
    Date created: 25/05/2021
    Python Version: 3.9

"""

from turtle import Turtle
import random

COLORS = ["blue", "orange", "red", "purple", "black", "pink", "coral", "DarkCyan", "CadetBlue", "DarkGreen"]


class CountryName(Turtle):

    # This class creates a turtle and sends it to the given coordinates.
    # It takes coordinates and country size as parameters.
    def __init__(self, x, y, country_name, size):
        super().__init__()
        color = random.choice(COLORS)
        self.hideturtle()
        self.penup()
        self.color(color)
        self.goto(int(x), int(y))

        # Adjusts the font size according to the country size.
        fontsize = 18
        if size == "middle":
            fontsize = 12
        elif size == "small":
            fontsize = 8

        my_font = ("Courier", fontsize, "normal")
        self.write(country_name, align="center", font=my_font)
