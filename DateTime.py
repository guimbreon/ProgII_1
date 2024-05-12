#-*- coding: utf-8 -*-

# 2023-2024 Programação 2 (LTI)
# Grupo 13
#62372 Guilherme Soares
#62242 Adriano Neves
from constants import *
import copy

class DateTime:
    """
    Class for handling date and time operations.
    """

    def __init__(self, time):
        """
        Initialize DateTime object.

        Args:
        - time (str): String representing a time in the format "HHhMM".
        """
        self._time = time

    def hourToList(self):
        """
        Split the time string into hours and minutes and convert them to integers.

        Returns:
        - list: List containing hours and minutes as integers.
        """
        time = (self._time).replace("\n", "").split("h")
        return [int(time[0]), int(time[1])]

    def nextDay(self):
        """
        Calculate the next day based on the given date.

        Returns:
        - str: String representing the next day in the format "DD:MM:YYYY\n".
        """
        date = self._time
        date = date.split(":")
        day = int(date[DAY])
        month = int(date[MONTH])
        year = int(date[YEAR])
        if day == 30:
            day = 1
            if month == 12:
                month = 1
                year = year + 1
            else:
                month = month + 1
        else:
            day = day + 1
        return f"{day}:{month}:{year}\n"

    def hourToInt(time):
        """
        Convert the given time string into an integer representing hours.

        Args:
        - time (str): String representing a time in the format "HHhMM".

        Returns:
        - int: Integer representing the hours.
        """
        t = time.split("h")
        return int(t[0])

    def minutesToInt(time):
        """
        Convert the given time string into an integer representing minutes.

        Args:
        - time (str): String representing a time in the format "HHhMM".

        Returns:
        - int: Integer representing the minutes.
        """
        t = time.split("h")
        return int(t[1])

    def intToTime(hour, minutes):
        """
        Convert hours and minutes into a time string.

        Args:
        - hour (int): Integer representing hours.
        - minutes (int): Integer representing minutes.

        Returns:
        - str: String representing the time in the format "HHhMM".
        """
        if hour != "w":
            h = str(hour)
            m = str(minutes)

            if hour < 10:
                h = "0" + h

            if minutes < 10:
                m = "0" + m

            return h + "h" + m
        else:
            return "weekly leave"

    def add30Min(oldSched):
        """
        Add 30 minutes to the given time.

        Args:
        - oldSched (list): List containing hours and minutes of the previous schedule.

        Returns:
        - list: List containing updated hours and minutes after adding 30 minutes.
        """
        oldSched[1] += 30
        if oldSched[1] >= 60:
            oldSched[0] += 1
            oldSched[1] = 0 
            
        return oldSched
