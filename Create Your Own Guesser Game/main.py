"""
    Project name: Create Your Own Guesser Game
    Author: Ömer Ünal
    Date created: 25/05/2021
    Python Version: 3.9

"""

import pandas
import turtle
from dataName import DataName

# Initialize image name and title
IMAGE = "example.gif"
TITLE = "Guess Game"

# Creates screen with title US States Game
screen = turtle.Screen()
screen.title(TITLE)
# Import picture to our screen
image = IMAGE
screen.addshape(image)
turtle.shape(image)

# Import states csv and save state names to list
data = pandas.read_csv("data.csv")
all_answers = data.name.to_list()


correct_answers = 0
guessed_list = []

# Continue the game until the player correctly guesses all states.
while correct_answers < len(all_answers):
    answer = screen.textinput(title=f"{correct_answers}/{len(all_answers)} States Correct",
                              prompt="What's another state's name?").lower()

    # If the player writes "Exit", end the game.
    if answer == "Exit":
        break

    # Check if guess is in states
    if answer in all_answers and answer not in guessed_list:
        x = data[data.name == answer].x
        y = data[data.name == answer].y

        # Append guess to guessed list so that we can check if user guess it twice
        guessed_list.append(answer)
        correct_answers += 1
        # Create turtle from StateName class
        state_name = DataName(x, y, answer)

turtle.mainloop()

# Add the states the player forgot to the list and write them to the file to show the player.
forgotten_answers = [item for item in all_answers if item not in guessed_list]
data_last = pandas.DataFrame(forgotten_answers)
data_last.to_csv("Forgotten.csv")
