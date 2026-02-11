import os
import pathlib
import random
import time
import models
import views


def validate_directory(directory: pathlib.Path):
    """
    Validate the directory path
    Raises:
        FileNotFoundError: If the directory does not exist
        NotADirectoryError: If the path is not a directory
        PermissionError: If the directory is not readable
    """
    if not directory.exists():
        raise FileNotFoundError(f"Specified directory '{directory}' does not exist")
    if not directory.is_dir():
        raise NotADirectoryError(f"Specified path '{directory}' is not a directory")
    if not os.access(directory, os.R_OK):
        raise PermissionError(f"Specified directory '{directory}' is not readable")


# ==============================
# Movies importation function
# ==============================

def import_movie_list(directory: pathlib.Path):
    """
    Import and return the list of movies from the directory

    Returns:
        list: List of movie filenames
    """

    files = []
    import_dir = os.listdir(directory)

    for file in import_dir:
        files.append(file)
    return files


# ==============================
# Select the movie function
# ==============================

def get_movie(list):
    """
    Get a random movie from the list

    Args:
        list: List of movie filenames

    Returns:
        Movie: A random Movie instance
    """

    suggest_nb = random.randint(0, len(list) - 1)
    my_movie = models.movie_handler(os.path.splitext(list[suggest_nb])[0])
    return my_movie


# ==============================
# Silent mode function
# ==============================

def run_silent_mode(movies_list: list):
    """
    Run the silent mode of the movie suggester

    In silent mode, the program suggests movies without animations.
    The user can accept, pass, or mark as watched.
    After 5 passes, the user is banned.

    Returns:
        UserChoice.ACCEPT if user accepts a movie,
        UserChoice.PASS if too many passes,
        Status.ERROR if user types wrong value
    """

    nb_proposal = 1
    state: models.UserChoice | models.Status | None = None

    views.display_message(views.sm_presentation)
    while state is None:
        my_movie = get_movie(movies_list)
        views.display_message(views.sm_suggestion.
                              format(movie_name=my_movie.name()))
        answer = views.sm_answer()
        if answer == models.UserChoice.PASS:
            my_movie.set_rejected_count(1)
            nb_proposal += 1
            if nb_proposal == 6:
                state = models.UserChoice.PASS
        elif answer == models.UserChoice.ACCEPT:
            state = models.UserChoice.ACCEPT
        elif answer == models.UserChoice.WATCHED:
            my_movie.set_watched(True)
        elif answer in (models.Status.ERROR, models.Status.INVALID_INPUT):
            print("You lost 1 proposal!")
            print("Be carefull!!!")
            nb_proposal += 1
            if nb_proposal == 6:
                state = models.Status.ERROR
    return state


# ==============================
# Normal mode helpers
# ==============================

def _display_movie_prompt(movie):
    """Display movie name with formatted prompt"""
    print("=================")
    print(" ")
    views.type_writer(f"{movie.name()}")
    print(" ")
    print("=================")
    views.type_writer("What do you want to do?")


def _handle_pass_answer(movie, nb_proposal, refusal_messages):
    """Handle PASS answer: increment rejection, show message, check limit"""
    movie.set_rejected_count(1)
    # Show escalating refusal messages for proposals 1-4
    if nb_proposal in refusal_messages:
        message = refusal_messages[nb_proposal]
        views.type_writer(views.get_random_nm_message(message))
    nb_proposal += 1
    # Ban after 5 rejections
    state = models.UserChoice.PASS if nb_proposal == 6 else None
    return nb_proposal, state


def _handle_watched_answer(movie):
    """Handle WATCHED answer: mark as watched and show message"""
    movie.set_watched(True)
    message = views.get_random_nm_message(views.nm_watched_messages)
    views.type_writer(message)


def _handle_error_answer(nb_proposal):
    """Handle ERROR answer: show message, increment, check limit"""
    views.type_writer("So...You lost 1 try!")
    nb_proposal += 1
    state = models.Status.ERROR if nb_proposal == 6 else None
    return nb_proposal, state


def normal_answer_loop(list, state):
    """
    Handle the movie suggestion loop in normal mode

    Presents movies one by one and handles user responses.
    Shows escalating refusal messages (1-4) based on rejection count.
    Bans the user after 5 rejections.

    Args:
        list: List of movie filenames
        state: Current state (None until user accepts or gets banned)

    Returns:
        UserChoice: ACCEPT if user accepts, PASS if user gets banned
    """
    nb_proposal = 1
    # Map proposal number to corresponding refusal message tuple
    refusal_messages = {
        1: views.nm_refusal_1,
        2: views.nm_refusal_2,
        3: views.nm_refusal_3,
        4: views.nm_refusal_4
    }

    while state is None:
        my_movie = get_movie(list)
        _display_movie_prompt(my_movie)
        answer = views.nm_answer()

        # Handle user's choice
        if answer == models.UserChoice.PASS:
            nb_proposal, state = _handle_pass_answer(
                my_movie, nb_proposal, refusal_messages
            )
        elif answer == models.UserChoice.ACCEPT:
            state = models.UserChoice.ACCEPT
        elif answer == models.UserChoice.WATCHED:
            _handle_watched_answer(my_movie)
        elif answer in (models.Status.ERROR, models.Status.INVALID_INPUT):
            nb_proposal, state = _handle_error_answer(nb_proposal)

        if state is not None:
            return state


# ==============================
# Normal mode function
# ==============================

def run_normal_mode(list):
    """
    Run the normal mode of the movie suggester

    Normal mode features a sarcastic, depressive bot personality with:
    - Theatrical introduction with typewriter effects
    - User consent requirement to continue
    - Escalating responses to rejections
    - Dramatic movie reveal sequence

    Args:
        list: List of movie filenames

    Returns:
        UserChoice: Final state (ACCEPT or PASS)
    """
    end = False
    state = None

    while not end:

        # Display title banner
        print("**********************")
        print("***                ***")
        print("***  Pick or Die!  ***")
        print("***                ***")
        print("**********************")

        # Introduction sequence
        for msg in views.starting_messages:
            views.type_writer(msg)
            time.sleep(0.7)

        time.sleep(2)
        views.type_writer("I'm waiting!")

        # Get user consent
        time.sleep(1)
        for msg in views.answer_message:
            views.type_writer(msg)
            time.sleep(0.7)

        answer = input("answer....please: \n")

        # Handle rejection of consent
        if answer != "yes" and answer != "y":
            views.type_writer(
                "Told you to put yes or y and look what you've done. "
                "Traitor...*sniff* *sniff*"
            )
            time.sleep(2)
            views.type_writer(
                "You will burn in Paul W. S. Anderson movie."
            )
            time.sleep(1)
            end = True
            continue  # Exit loop immediately without showing rules or movies

        # Explain the rules
        for msg in views.rule_message:
            views.type_writer(msg)
            time.sleep(0.7)

        # Dramatic movie reveal
        views.type_writer("Drumroll, please...")
        time.sleep(2)

        for msg in views.movie_message:
            views.type_writer(msg)
            time.sleep(0.7)

        # Start the suggestion loop
        state = normal_answer_loop(list, state)
        end = True

    return state
