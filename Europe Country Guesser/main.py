"""
    Project name: Europe Country Guesser
    Author: Ömer Ünal
    Date created: 25/05/2021
    Python Version: 3.9

"""

import pandas
import turtle
from countryName import CountryName

# Creates screen with title Europe Country Game
screen = turtle.Screen()
screen.title("Europe Country Game")
screen.setup(1280, 1024)
# Import picture to our screen
image = "europe.gif"
screen.addshape(image)
turtle.shape(image)

# Import europe csv and save countries names to list
data = pandas.read_csv("europe.csv")
all_countries = data.country.to_list()

correct_countries = 0
guessed_country = []

# Continue the game until the player correctly guesses all countries.
while correct_countries < 38:
    answer_country = screen.textinput(title=f"{correct_countries}/{len(all_countries)} Countries Correct",
                                      prompt="What's another country's name?").lower()

    # If the player writes "exit", end the game.
    if answer_country == "exit":
        break

    # Check if guess is in states
    if answer_country in all_countries and answer_country not in guessed_country:
        x = data[data.country == answer_country].x
        y = data[data.country == answer_country].y
        size = data[data.country == answer_country].csize.item()

        # Append guess to guessed list so that we can check if user guess it twice
        guessed_country.append(answer_country)
        correct_countries += 1
        # Create turtle from CountryName class
        country_name = CountryName(x, y, answer_country, size)

turtle.mainloop()

# Add the countries the player forgot to the list and write them to the file to show the player.
forgotten_country = [item for item in all_countries if item not in guessed_country]
data_last = pandas.DataFrame(forgotten_country)
data_last.to_csv("Forgotten Countries.csv")
