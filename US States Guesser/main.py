"""
    Project name: US States Guesser
    Author: Ömer Ünal
    Date created: 25/05/2021
    Python Version: 3.9

"""

import pandas
import turtle
from stateName import StateName

# Creates screen with title US States Game
screen = turtle.Screen()
screen.title("US States Game")
screen.setup(750, 550)
# Import picture to our screen
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Import states csv and save state names to list
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

correct_states = 0
guessed_states = []

# Continue the game until the player correctly guesses all states.
while correct_states < len(all_states):
    answer_state = screen.textinput(title=f"{correct_states}/{len(all_states)} States Correct",
                                    prompt="What's another state's name?").title()

    # If the player writes "Exit", end the game.
    if answer_state == "Exit":
        break

    # Check if guess is in states
    if answer_state in all_states and answer_state not in guessed_states:
        x = data[data.state == answer_state].x
        y = data[data.state == answer_state].y

        # Append guess to guessed list so that we can check if user guess it twice
        guessed_states.append(answer_state)
        correct_states += 1
        # Create turtle from StateName class
        state_name = StateName(x, y, answer_state)

turtle.mainloop()

# Add the states the player forgot to the list and write them to the file to show the player.
forgotten_states = [item for item in all_states if item not in guessed_states]
data_last = pandas.DataFrame(forgotten_states)
data_last.to_csv("Forgotten States.csv")
