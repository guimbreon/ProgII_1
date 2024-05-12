#-*- coding: utf-8 -*-

# 2023-2024 Programação 2 (LTI)
# Grupo 13
#62372 Guilherme Soares
#62242 Adriano Neves
from constants import *
from DateTime import DateTime

class Schedule:
    """
    Class representing a schedule entry with time, month, and doctor information.
    """

    def __init__(self, schedule):
        """
        Initialize a Schedule object.

        Args:
            schedule (list): A list containing schedule information.
                Expected structure: [time, moth, doc]
        """
        self._time = schedule[REQ_TIME_IDX]
        self._moth = schedule[REQ_MOTH_IDX]
        self._doc = schedule[REQ_DOC_IDX]
        self._list = schedule

    def __str__(self):
        """
        Get the string representation of the schedule object.

        Returns:
            str: String representation of the schedule.
        """
        return "[[" + str(self._time[0]) + ", " + str(self._time[1]) + "], " + self._moth + ", " + self._doc + "]"

    def getSchd(self):
        """
        Get the schedule list.

        Returns:
            list: List containing schedule information.
        """
        return self._list
    
    def getTime(self):
        """
        Get the time of the schedule.

        Returns:
            str: The time of the schedule.
        """
        return self._time

    def setTime(self, value):
        """
        Set the time of the schedule.

        Args:
            value (str): The new time value.
        """
        self._time = value

    def getMoth(self):
        """
        Get the month of the schedule.

        Returns:
            str: The month of the schedule.
        """
        return self._moth

    def setMoth(self, value):
        """
        Set the month of the schedule.

        Args:
            value (str): The new month value.
        """
        self._moth = value

    def getDoc(self):
        """
        Get the doctor of the schedule.

        Returns:
            str: The doctor of the schedule.
        """
        return self._doc

    def setDoc(self, value):
        """
        Set the doctor of the schedule.

        Args:
            value (str): The new doctor value.
        """
        self._doc = value
