#-*- coding: utf-8 -*-

# 2023-2024 Programação 2 (LTI)
# Grupo 13
#62372 Guilherme Soares
#62242 Adriano Neves
from constants import *

class Mother:
    """
    A class that represents a mother and stores relevant data about her.

    Attributes:
        _name (str): The name of the mother.
        _age (str): The age of the mother.
        _wrist (str): The wrist color of the mother.
        _imp (str): The level of importance of the mother.
    """

    def __init__(self, mother):
        """
        Initializes a Mother object with the provided data.

        Args:
            mother (list): A list containing the mother's data, where:
                           - mother[MOTH_NAME_IDX] is the name,
                           - mother[MOTH_AGE_IDX] is the age,
                           - mother[MOTH_WRIST_IDX] is the wrist color, and
                           - mother[MOTH_IMP_IDX] is the level of importance.
        """
        self._name = mother[MOTH_NAME_IDX]
        self._age = mother[MOTH_AGE_IDX]
        self._wrist = mother[MOTH_WRIST_IDX]
        self._imp = mother[MOTH_IMP_IDX]
        self._mother = mother

    def __str__(self):
        """
        Returns a string representation of the Mother object.

        Returns:
            str: A string representation of the Mother object.
        """
        return "[" + self._name + ", " + self._age + ", " + str(self._wrist) + ", " + str(self._imp) + "]"
    
    def getMother(self):
        """
        Get the list representation of the mother's data.

        Returns:
            list: A list containing the mother's data.
        """
        return self._mother

    def getName(self):
        """
        Returns the name of the mother.

        Returns:
            str: The name of the mother.
        """
        return self._name
    
    def setName(self, newValue):
        """
        Sets the name of the mother to the specified value.

        Args:
            newValue (str): The new name for the mother.
        """
        self._name = newValue
    
    def getAge(self):
        """
        Returns the age of the mother.

        Returns:
            str: The age of the mother.
        """
        return self._age
    
    def setAge(self, newValue):
        """
        Sets the age of the mother to the specified value.

        Args:
            newValue (str): The new age for the mother.
        """
        self._age = newValue
    
    def getWrist(self):
        """
        Returns the wrist color of the mother.

        Returns:
            str: The wrist color of the mother.
        """
        return self._wrist
    
    def setWrist(self, newValue):
        """
        Sets the wrist color of the mother to the specified value.

        Args:
            newValue (str): The new wrist color for the mother.
        """
        self._wrist = newValue
    
    def getImp(self):
        """
        Returns the level of importance of the mother.

        Returns:
            str: The level of importance of the mother.
        """
        return self._imp
    
    def setImp(self, newValue):
        """
        Sets the level of importance of the mother to the specified value.

        Args:
            newValue (str): The new level of importance for the mother.
        """
        self._imp = newValue
