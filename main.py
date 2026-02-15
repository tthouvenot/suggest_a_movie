"""
Main Module - Entry point for the Movie Suggester application

This application suggests random movies from a network directory.
It offers two modes:
- Silent mode: Clean, straightforward suggestions
- Normal mode: Sarcastic bot with escalating responses
"""
VERSION = "0.1"

import models
import views
import controllers
import argparse
import pathlib


def ask_silent_mode():
    """
    Ask the user if he wants to run in silent mode
    Returns:
        bool: True if user wants to run in silent mode
    """
    # Ask user for mode selection
    print("================================")
    answer = input("Do you want to use silent mode? (y/n)\n")
    print("================================")
    return answer.lower() in ("y", "yes")


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--silent", help="Run in silent mode", required=False)
    parser.add_argument("-d", "--directory", help="Path to the directory where films are stored",
                        default=pathlib.Path.home(), required=False)
    parser.add_argument("-v", "--version", help="Show version",
                        action="version", version=VERSION)
    args = parser.parse_args()

    # Initialize variables-------------------
    state: models.UserChoice | models.Status | None = None
    movies_list: list
    silent_mode: bool
    # ----------------------------------------

    films_directory = args.directory
    if type(films_directory) is str:
        films_directory = pathlib.Path(films_directory)

    # Import movies list---------------------
    try:
        controllers.validate_directory(films_directory)
    except (FileNotFoundError, NotADirectoryError, PermissionError) as e:
        print(f'Error!\n{e}')
        exit(1)
    movies_list = controllers.import_movie_list(films_directory)

    is_silent_mode_specified = "silent" in args
    print(args)
    silent_mode = args.silent
    if not is_silent_mode_specified:
        silent_mode = ask_silent_mode()
    # ----------------------------------------

    try:
        # Run selected mode
        if silent_mode:
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
    except KeyboardInterrupt:
        print("Bye!")
        exit(0)
    except Exception as e:
        raise e
