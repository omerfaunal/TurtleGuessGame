"""
    File name: gameCreationEngine
    Author: Ömer Ünal
    Date created: 25/05/2021
    Python Version: 3.9

"""

import pandas
import turtle

"""
To create your game, first add the answers to the list in the order you click on the screen.
Then click the locations of all the answers and close the screen.
After doing these steps, you can play the game from the main section.
"""

# Initialize image name
IMAGE = "example.gif"
# Add the answers to this list in the order you click on the coordinates.
answers = ["answer1", "answer2"]

# Creates screen with title US States Game
screen = turtle.Screen()
# Import picture to our screen
image = IMAGE
screen.addshape(image)
turtle.shape(image)

coor_x = []
coor_y = []


def mouse_click_coor(x, y):
    print(x, y)
    coor_x.append(x)
    coor_y.append(y)


# This part detects when you click somewhere in the screen
turtle.onscreenclick(mouse_click_coor)

turtle.mainloop()

data_dict = {"name": answers,
             "x": coor_x,
             "y": coor_y}


data = pandas.DataFrame(data_dict)
data.to_csv("data.csv")
