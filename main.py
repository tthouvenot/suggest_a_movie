"""
Main Module - Entry point for the Movie Suggester application

This application suggests random movies from a network directory.
It offers two modes:
- Silent mode: Clean, straightforward suggestions
- Normal mode: Sarcastic bot with escalating responses
"""

import models
import views
import controllers


# Initialize variables
silent_mode = False
state = None

try:
    movies_list = controllers.import_movie_list()
except FileNotFoundError:
    print("File path does not exist")
    exit()
except PermissionError:
    print("Permission denied to access directory")
    exit()

# Ask user for mode selection
print("================================")
answer = input("Do you want to use silent mode? (y/n)\n")
print("================================")

# Run selected mode
if answer.lower() in ("y", "yes"):
    silent_mode = True
    state = controllers.run_silent_mode(movies_list)
else:
    state = controllers.run_normal_mode(movies_list)

# Display final messages based on user's choice
if state == models.UserChoice.ACCEPT:
    if silent_mode:
        views.display_message(views.sm_accept)
    else:
        views.type_writer(
            views.get_random_nm_message(views.nm_accepted_messages)
        )
elif state == models.UserChoice.PASS:
    if silent_mode:
        views.display_message(views.sm_banned)
    else:
        views.type_writer(
            views.get_random_nm_message(views.nm_banned_messages)
        )
elif state == models.Status.ERROR:
    if silent_mode:
        print("Unfortunately you type the wrong value and get the max "
              "proposal amount!")
    else:
        views.type_writer(
            "Not only do you reject my choices, but you can't "
            "even type properly?\n"
            "Go away!\n"
            "No...Don't leave me alone! Come back soon\n"
            "See ya"
        )
