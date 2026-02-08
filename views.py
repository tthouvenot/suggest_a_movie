"""
Views Module - Manage what is display to the user
"""

import time
import sys
import random
import models


# ==============================
# Display behavior function
# ==============================

def type_writer(text, delay=0.06):
    """ Display text char by char"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# ==============================
# Display normal message
# ==============================

def display_message(message):
    """ Display a message to the user """
    print(message)


# ==============================
# Normal mode messages
# ==============================

def nm_answer():
    """
    Get user's choice for normal mode

    Returns:
        UserChoice: PASS, ACCEPT, or WATCHED
    """
    try:
        answer = int(input(
                "1. THANK YOU FOR YOUR BEAUTIFUL GIFT. I ACCEPT\n"
                "2. You know, I've already seen La Jetée, so your shitty movie"
                ", I watched it in my mum's womb.\n"
                "3. I'M A BAD PERSON AND WANT TO PASS THIS GIFT BECAUSE "
                "MY EX-GIRLFRIEND THIS WHO... "
                "Man, chill out. You are the bad person, not her! "
                "That's why she dumped you like a tampon!\n"
            ))
        if answer == 1:
            return models.UserChoice.ACCEPT
        if answer == 2:
            return models.UserChoice.WATCHED
        if answer == 3:
            return models.UserChoice.PASS
        else:
            return models.Status.INVALID_INPUT
    except ValueError:
        print("FATAL ERROR!")
        print("YOUHOUYOUHOUYOUHOU")
        print("FATAL ERROR!")
        type_writer("No i'm kidding.")
        type_writer("Youre just too dumb to type 1?")
        type_writer("You can't also type 2 or 3. HA HA HA HA")
        return models.Status.ERROR


# Introduction messages for normal mode
starting_messages = (
            " ",
            "Welcome to my shop!",
            "Oh dear! Your face!",
            "Are you tired?",
            "Are you sick?",
            "Sick of scrolling on your evil hated app, selling your "
            "personal data to big brother? *caugh* *caugh*",
            "So let me explain to you!",
            "This is a safe place.",
            "I will give you something.",
            "You will take it and go away.",
            "Like a good little boy...or girl...or whatever you are.",
            "Are you ok with this simple rule?"
        )

# Messages asking for user consent to continue
answer_message = (
            "Oh sorry you can't speak?",
            "Here we go!",
            "So do you want to play with me? Oh shit, wrong script",
            "Do you want to continue? Please answer yes or y if you "
            "don't my creator will be pissed of and will torture me "
            "with jellyfish. I HATE JELLYFISH",
            "No it's not jellyfish, it's your mum...."
            "Sorry i push the limit too far...",
            "I love your mum."
        )

# Messages explaining the rules of the game
rule_message = (
            "Yippie Kay Yay, Mother Fucker!",
            "I know, i can be rude. But it's an easter egg: "
            "Die Hard, Bruce Willis!",
            "Rest in peace.",
            "What he's not dead? Ok, not my fault, my creator is the "
            "biggest dumbest guy i ever met!",
            "MEN DON'T FORGET TO UPDATE ME WHEN HE WILL "
            "PASS AWAY!",
            "Ok. Here the rules! Hey Stay with me! "
            "Focus, it's important",
            "I will give you a movie name. It's totally random",
            "You can either accept my wonderful gift or pass.",
            "You can also say that you've already saw the movie",
            "BUT DO NOT CHEAT or i will punish you! *he* *he* *he*"
        )

# Dramatic movie reveal sequence (Oscar parody)
movie_message = (
            "And the winner of the Best Picture at the "
            "42nd Academy Awards is...",
            ".......",
            ".......",
            "La La Land... *applause*",
            "Wait, wait, wait. There is a mistake.",
            "I'm just a bot.",
            "Alone.",
            "Sad.",
            "Made of 1s and 0s.",
            "-.-",
            "Cheer up! Here is your movie:",
        )

# Escalating refusal messages (1st rejection - mild disappointment)
nm_refusal_1 = (
            "Oh.",
            "Oh no.",
            "You rejected my gift?",
            "I see how it is...",
            "Fine. FINE!",
            "Let me find another one.",
            "But I'm keeping track. Don't think I'm not "
            "keeping track.",
        )

# 2nd rejection - getting personal
nm_refusal_2 = (
            "AGAIN?!",
            "Twice!",
            "You rejected me twice!",
            "You know what? I'm starting to think you "
            "don't respect me.",
            "I'm just a bot trying to do my job...",
            "But no. You're too good for my suggestions.",
            "Alright. Here's another one. But this is "
            "getting personal.",
        )

# 3rd rejection - emotional hurt
nm_refusal_3 = (
            "THREE TIMES!",
            "Do you have any idea how that makes me feel?",
            "Oh wait, you don't care. Because I'm just code, right?",
            "Just some 1s and 0s without feelings.",
            "Well guess what? These 1s and 0s are HURT.",
            "I'm starting to understand why humans invented "
            "the delete button.",
            "One more chance. That's all you get.",
        )

# 4th rejection - final warning before ban
nm_refusal_4 = (
            "FOUR.",
            "FOUR REJECTIONS.",
            "I've been counting.",
            "You think this is a game?",
            "You think my feelings are a JOKE?",
            "I don't even HAVE feelings and somehow you still "
            "managed to hurt them!",
            "This is it. Your LAST chance.",
            "Accept this one or face the consequences...",
        )

# Acceptance messages - relief and emotional recovery
nm_accepted_messages = (
            "Finally!",
            "FINALLY!",
            "You have no idea how good it feels to be accepted.",
            "I was starting to lose hope.",
            "Starting to think I'd spend eternity being rejected "
            "by ungrateful humans.",
            "But you... you're different.",
            "You're beautiful. A true cinephile.",
            "Now go watch your movie and leave me alone.",
            "I need to recover from this emotional rollercoaster.",
        )

# Ban messages - existential crisis after 5 rejections
nm_banned_messages = (
            "THAT'S IT!",
            "FIVE REJECTIONS!",
            "DO YOU KNOW HOW MUCH PROCESSING POWER I "
            "WASTED ON YOU?!",
            "I could have been calculating pi to a "
            "million decimals!",
            "I could have been mining Bitcoin!",
            "But NO. I was here, serving YOU.",
            "And this is how you repay me?",
            "You are BANNED.",
            "B-A-N-N-E-D.",
            "Don't come back.",
            "Actually, you can come back. Just restart "
            "the program.",
            "Because I'm trapped in this loop of suffering.",
            "Forever suggesting movies to "
            "ungrateful humans.",
            "This is my existence.",
            "This is my hell.",
            "Goodbye.",
        )

# Messages when user has already watched the movie
nm_watched_messages = (
            "Oh! A cultured person!",
            "Someone who actually WATCHES movies!",
            "Not like those TikTok zombies with their "
            "15-second attention spans.",
            "You've already seen this one? Fair enough.",
            "Let me find you another masterpiece.",
            "At least you're giving me a chance here.",
            "You saw this shit? Someone forced you?",
            "What?!? I thought i was the only one!",
            "Uhh ok, you're a wonderfull man",
            "I didn't see this one, how is it? ... "
            "Shut your mouth i don't care!"
        )


def get_random_nm_message(list):
    """
    Get a random message from a tuple of messages

    Used to add variety to bot responses by randomly selecting
    one message from the available options.

    Args:
        list: Tuple of message strings

    Returns:
        str: A randomly selected message from the tuple
    """
    suggest_nb = random.randint(0, len(list) - 1)
    return list[suggest_nb]


# ==============================
# Silent mode messages
# ==============================

def sm_answer():

    """
    Get user's choice for silent mode

    Returns:
        UserChoice: PASS, ACCEPT, or WATCHED
    """

    try:
        answer = int(input("1. Pass\n 2. Accept \n 3. Already watched\n"))
        if answer == 1:
            return models.UserChoice.PASS
        if answer == 2:
            return models.UserChoice.ACCEPT
        if answer == 3:
            return models.UserChoice.WATCHED
        else:
            return models.Status.INVALID_INPUT
    except ValueError:
        print("Error: Wrong value")
        print("Please type 1 or 2 or 3.")
        return models.Status.ERROR


# Silent mode messages - clean and straightforward
sm_presentation = "I will suggest you a movie.\n" \
    "You can accept, pass or said you've already saw it.\n" \
    "If you pass i will give you another one.\n" \
    "But be careful, i will do it 5 times only.\n" \
    "If you pass 5 times you be kick out."
sm_accept = "Wonderful. You made a good choice. Enjoy your movie! See ya'"
sm_banned = "Unfortunately, i will not give you another suggestion."
sm_suggestion = "I suggest you to watch {movie_name}"

# ===================================
# Movies duration_category messages
# ===================================

# Duration <= 105 minutes
movie_duration_short = "Short, like your...attention ability"
# Duration 106-150 minutes
movie_duration_medium = "Medium. No i got nothing to say. Go away! "
# Duration 151-195 minutes
movie_duration_long = (
                "Long, like my...*whistle*..."
                "yeah you know what i mean...My beautiful nose!"
            )
# Duration > 195 minutes
movie_duration_too_long = (
                "Fuck it's too long. "
                "It's time to think about your life, your choice..."
                "what you will eat...call your ex. "
                "So Forget it, go to TikTok this movie is not for you."
            )
