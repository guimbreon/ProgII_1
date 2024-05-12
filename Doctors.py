#-*- coding: utf-8 -*-

# 2023-2024 Programação 2 (LTI)
# Grupo 13
#62372 Guilherme Soares
#62242 Adriano Neves
from constants import *
from DateTime import DateTime
import copy

class Doctors():
    '''
    Class representing a doctor with information about name, category, working hours, consultation duration, and total working time.

    Attributes:
        _name (str): The name of the doctor.
        _cat (int): The category of the doctor.
        _time (str): The working hours of the doctor.
        _mins (int): The duration of the consultation in minutes.
        _totaltime (str): The total working time of the doctor.
    '''
    def __init__(self, doctor):
        '''
        Constructor method for the Doctors class.

        Args:
            doctor (list): A list containing information about the doctor. The order of elements in the list should follow the order defined by the constants DOCT_NAME_IDX, DOCT_CAT_IDX, DOCT_TIME_IDX, DOCT_MINS_IDX, and DOCT_TOTALTIME_IDX.
        '''
        self._name = doctor[DOCT_NAME_IDX]
        self._cat = doctor[DOCT_CAT_IDX]
        self._time = doctor[DOCT_TIME_IDX]
        self._mins = doctor[DOCT_MINS_IDX]
        self._totaltime = doctor[DOCT_TOTALTIME_IDX]
        self._doctor = doctor

    def __str__(self):
        if self.getTime() == "weekly leave":
            return "[" + self.getName() + ", " + str(self.getCategory()) + ", " + self.getTime() + ", " + str(self.getMins()) + ", [" + str(self.getTotalTime()[0]) + ", " + str(self.getTotalTime()[1]) + "]]"
        else:
            return "[" + self.getName() + ", " + str(self.getCategory()) + ", [" + str(self.getTime()[0]) + ", " + str(self.getTime()[1]) + "], " + str(self.getMins()) + ", [" + str(self.getTotalTime()[0]) + ", " + str(self.getTotalTime()[1]) + "]]"

    def getDoctor(self):
        '''
        Get the doctor's information as a list.

        Returns:
            list: List containing the doctor's information.
        '''
        return [self.getName(),self.getCategory(),self.getTime(), self.getMins(), self.getTotalTime()]
    
    def getName(self):
        '''
        Get the name of the doctor.

        Returns:
            str: The name of the doctor.
        '''
        return self._name

    def setName(self, name):
        '''
        Set the name of the doctor.

        Args:
            name (str): The new name of the doctor.
        '''
        self._name = name

    def getCategory(self):
        '''
        Get the category of the doctor.

        Returns:
            int: The category of the doctor.
        '''
        return self._cat

    def setCategory(self, cat):
        '''
        Set the category of the doctor.

        Args:
            cat (int): The new category of the doctor.
        '''
        self._cat = cat

    def getTime(self):
        '''
        Get the working hours of the doctor.

        Returns:
            str: The working hours of the doctor.
        '''
        return self._time

    def setTime(self, time):
        '''
        Set the working hours of the doctor.

        Args:
            time (str): The new working hours of the doctor.
        '''
        self._time = time

    def getMins(self):
        '''
        Get the duration of the consultation in minutes.

        Returns:
            int: The duration of the consultation in minutes.
        '''
        return self._mins

    def setMins(self, mins):
        '''
        Set the duration of the consultation in minutes.

        Args:
            mins (int): The new duration of the consultation in minutes.
        '''
        self._mins = mins

    def getTotalTime(self):
        '''
        Get the total working time of the doctor.

        Returns:
            str: The total working time of the doctor.
        '''
        return self._totaltime

    def setTotalTime(self, totaltime):
        '''
        Set the total working time of the doctor.

        Args:
            totaltime (str): The new total working time of the doctor.
        '''
        self._totaltime = totaltime
        
    def add20Min(self):
        """
        Add 20 minutes to the doctor's time.
        """
        copieddoctor = copy.deepcopy(self)
        self._mins = str(int(self._mins) + 20)

        if int(self._mins) >= 240 and int(self._mins) < 260: #this way it's only the first time
            self._totaltime[0] += 1
            self._time[0] += 1
        self._time[1] += 20

        while self._time[1] >= 60:
            self._time[0] += 1
            self._time[1] -= 60
        
        self._totaltime[1] += 20

        while self._totaltime[1] >= 60:          
            self._totaltime[0] += 1
            self._totaltime[1] -= 60

        if self._totaltime[0] >= 40:
            self.setTime("weekly leave")

        elif self._time[0] >= 20:
            self._name = copieddoctor.getName()
            self._cat = copieddoctor.getCategory()
            self._time = copieddoctor.getTime()
            self._mins = copieddoctor.getMins()
            self._totaltime = copieddoctor.getTotalTime()
        self._totaltime = self._totaltime
