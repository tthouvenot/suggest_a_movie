"""
Models' Module - Datas and entities
"""

from enum import Enum
import views


# ==============================
# Enums (state flags)
# ==============================

class Status(Enum):

    """ Functions return status """
    OK = 0
    ERROR = 1
    NOT_FOUND = 2
    INVALID_INPUT = 3


class UserChoice(Enum):

    """ Proposal user choice """
    ACCEPT = 0
    PASS = 1
    WATCHED = 2


# ==============================
# Movies class and helpers
# ==============================

class Movie:
    """
    Define a movie with its metadata

    Attributes:
        _name (str): Movie title
        _year (int): Release year
        _decade (int): Decade of release
        _director (str): Director name
        _actors (str): Main actors
        _duration (int): Duration in minutes
        _duration_category (str): Category message based on duration
        _genre (str): Movie genre
        _watched (bool): Whether the movie has been watched
        _last_picked (str): Last time the movie was suggested
        _rejected_count (int): Number of times the movie was rejected
    """
    def __init__(self):
        self._name = None
        self._year = None
        self._decade = None
        self._director = None
        self._actors = None
        self._duration = None
        self._duration_category = None
        self._genre = None
        self._watched = None
        self._last_picked = None
        self._rejected_count = 0

    def name(self):
        return self._name

    def set_name(self, name):
        if not isinstance(name, str):
            return Status.INVALID_INPUT
        self._name = name

    def year(self):
        return self._year

    def set_year(self, year):
        try:
            year_int = int(year)
        except ValueError:
            print(f"{year} is not a valid value")
            return Status.INVALID_INPUT
        self._year = year_int

    def decade(self):
        return self._decade

    def set_decade(self):
        """
        Calculate and set the decade from the year

        Converts a year to its decade (e.g., 1995 -> 1990)
        Requires _year to be set first.
        """
        self._decade = (self._year // 10) * 10

    def director(self):
        return self._director

    def set_director(self, director):
        if not isinstance(director, str):
            return Status.INVALID_INPUT
        self._director = director

    def actors(self):
        return self._actors

    def set_actors(self, actors):
        if not isinstance(actors, str):
            return Status.INVALID_INPUT
        self._actors = actors

    def duration(self):
        return self._duration

    def set_duration(self, duration):
        try:
            duration_int = int(duration)
        except ValueError:
            print(f"{duration} is not a valid value")
            return Status.INVALID_INPUT
        self._duration = duration_int

    def duration_category(self):
        return self._duration_category

    def set_duration_category(self):
        """
        Categorize the movie based on its duration

        Categories:
        - Short: <= 105 minutes
        - Medium: 106-150 minutes
        - Long: 151-195 minutes
        - Too long: > 195 minutes

        Requires _duration to be set first.
        """
        if self._duration <= 105:
            self._duration_category = views.movie_duration_short
        elif self._duration <= 150:
            self._duration_category = views.movie_duration_medium
        elif self._duration <= 195:
            self._duration_category = views.movie_duration_long
        else:
            self._duration_category = views.movie_duration_too_long

    def genre(self):
        return self._genre

    def set_genre(self, genre):
        if not isinstance(genre, str):
            return Status.INVALID_INPUT
        self._genre = genre

    def watched(self):
        return self._watched

    def set_watched(self, watched):
        if not isinstance(watched, bool):
            return Status.INVALID_INPUT
        self._watched = watched

    def last_picked(self):
        return self._last_picked

    def set_last_picked(self, last_picked):
        if not isinstance(last_picked, str):
            return Status.INVALID_INPUT
        self._last_picked = last_picked

    def rejected_count(self):
        return self._rejected_count

    def set_rejected_count(self, count):
        """
        Increment the rejection counter

        Args:
            count: Number to add to the rejection count

        Returns:
            Status.INVALID_INPUT if count is not a valid integer,
            None otherwise
        """
        try:
            count_int = int(count)
        except ValueError:
            print(f"{count} is not a valid value")
            return Status.INVALID_INPUT
        self._rejected_count += count_int


def movie_handler(data):
    """
    Create the movie instance from data

    Args:
        data: The movie name/data to create the instance from

    Returns:
        MOVIE: a new movie instance if successful
        STATUS: Status.{VALUE} if something goes wrong
    """
    if data is None:
        return Status.NOT_FOUND
    new_movie = Movie()
    new_movie.set_name(data)
    return new_movie
