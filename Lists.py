#-*- coding: utf-8 -*-

# 2023-2024 Programação 2 (LTI)
# Grupo 13
#62372 Guilherme Soares
#62242 Adriano Neves
from constants import *
from Doctors import Doctors
from Schedule import Schedule
from Mother import Mother
import copy

class Lists:
    """
    A class for handling lists of various objects such as doctors, mothers, and schedules.
    """

    def __init__(self, list):
        """
        Initializes a Lists object with the given list.

        Args:
            list (list): A list containing objects.
        """
        self._list = list

    def getList(self):
        """
        Get the list contained in the Lists object.

        Returns:
            list: The list contained in the Lists object.
        """
        return self._list
    
    def sortSchedule(self):
        """
        Sorts a list of schedules based on time.

        Returns:
            list: A new list of schedules sorted by time.
        """
        schedules = self._list
        schd = []
        for item in schedules:
            schd.append(item.getSchd())
        orderedSchd = sorted(schd, key=lambda sched: (sched[0][0], sched[0][1]))

        schdOO = []
        for item in orderedSchd:
            schdOO.append(Schedule(item))
        return schdOO
    
    def sortDoctor(self):
        """
        Sorts a list of doctors.

        Returns:
            list: A new list of doctors sorted based on specific criteria.
        """
        finalDoctors = []
        doneWorking = []
        working = []
        for item in self._list:
            doctor = item.getDoctor()

            if doctor[DOCT_TIME_IDX] == "weekly leave":
                doneWorking.append(doctor)
            else:
                working.append(doctor)

        finalDoctors = sorted(working, key=lambda x: (int(x[DOCT_TIME_IDX][0]), int(x[DOCT_TIME_IDX][1]), -int(x[DOCT_CAT_IDX]), int(x[DOCT_MINS_IDX]), int(x[DOCT_TOTALTIME_IDX][0]), int(x[DOCT_TOTALTIME_IDX][1]), x[DOCT_NAME_IDX]))
        
        if len(doneWorking) > 0:
            doneWorking = sorted(doneWorking, key=lambda doctor: (-int(doctor[DOCT_CAT_IDX]), int(doctor[DOCT_MINS_IDX]), int(doctor[DOCT_TOTALTIME_IDX][0]), int(doctor[DOCT_TOTALTIME_IDX][1]), doctor[DOCT_NAME_IDX]))
            finalDoctors += doneWorking
        
        finalDoctorsOO = []

        for doctor in finalDoctors:

            finalDoctorsOO.append(Doctors(doctor))

        self.setList(finalDoctorsOO)

        return finalDoctorsOO
    
    def sortMothers(self):
        """
        Sorts a list of mothers based on specific criteria.

        Returns:
            list: A new list of mothers sorted based on importance, wrist color, age, and name.
        """
        newList = []
        for item in self._list:
            mother = item.getMother()
            if mother[MOTH_WRIST_IDX] == "green":
                mother[MOTH_WRIST_IDX] = 1
            elif mother[MOTH_WRIST_IDX] == "yellow":
                mother[MOTH_WRIST_IDX] = 2
            else:
                mother[MOTH_WRIST_IDX] = 3

            if mother[MOTH_IMP_IDX] == "low":
                mother[MOTH_IMP_IDX] = 1
            elif mother[MOTH_IMP_IDX] == "medium":
                mother[MOTH_IMP_IDX] = 2
            else:
                mother[MOTH_IMP_IDX] = 3
            newList.append(mother)
        requestsData = sorted(newList, key=lambda x: (-int(x[MOTH_IMP_IDX]), -int(x[MOTH_WRIST_IDX]), -int(x[MOTH_AGE_IDX]), x[MOTH_NAME_IDX]))
        finalDataOO = []

        for item in requestsData:
            finalDataOO.append(Mother(item))
        
        self.setList(finalDataOO)
    
    def setList(self, newList):
        """
        Sets the list contained in the Lists object to a new list.

        Args:
            newList (list): The new list to be set.
        """
        self._list = newList

    def updateSchedule(self, doctors, requests, previousSched, nextSched):
        """
        Updates the birth assistance schedule based on the given data.

        Args:
            doctors (list): A list of doctor objects.
            requests (list): A list of request objects.
            previousSched (list): A list representing the previous schedule.
            nextSched (str): The time of the next schedule.

        Returns:
            tuple: A tuple containing two lists:
                - A list of birth assistance requests representing the updated schedule.
                - A list of doctors with their updated times after being sorted for a given birth.
        """
        newRequests = []
        for sched in self._list:
            if sched.getTime() == nextSched or sched.getTime() > nextSched:
                newRequests.append(sched)
        schedule = copy.deepcopy(nextSched)
        for mother in requests:
            mother = mother.getMother()
            docNum = 0
            isItNotTreated = True
            for medic in doctors:
           
                medic = medic.getDoctor()

                if medic[DOCT_TIME_IDX] != "weekly leave":
                    if medic[DOCT_TIME_IDX][0] <= schedule[0] and medic[DOCT_TIME_IDX][1] < schedule[1] and isItNotTreated:
                        medic[DOCT_TIME_IDX] = copy.deepcopy(schedule)
                    copiedmedic = Doctors(copy.deepcopy(medic))
                    copiedmedic.add20Min()
                    
                    if copiedmedic != medic:
                        if ((int(mother[MOTH_IMP_IDX]) == 3 and int(medic[DOCT_CAT_IDX]) > 1) or (int(mother[MOTH_IMP_IDX]) < 3)) and isItNotTreated:
                            isItNotTreated = False
                            timeBegin = copy.deepcopy(medic[DOCT_TIME_IDX])
                            medicName = copy.deepcopy(medic[DOCT_NAME_IDX])
                            medic = Doctors(medic)
                            medic.add20Min()

                            doctors.pop(docNum)
                            doctors.append(medic)

                            doctors = Lists(doctors)
                            doctors = doctors.sortDoctor()

                            newRequests.append(Schedule([timeBegin, mother[MOTH_NAME_IDX], medicName]))
                docNum += 1
        newRequests = Lists(newRequests)
        newRequests.sortSchedule()
        doctors = Lists(doctors)
        doctors.sortDoctor()
        doctors.sortDocName()
        return newRequests.getList(), doctors.getList()
    
    def sortDocName(self):
        """
        Sorts the list of doctors by name.

        Returns:
            list: A new list of doctors sorted by name.
        """
        sortName = []
        for item in self._list:
            doctor = item.getDoctor()
            sortName.append(doctor)
        sortName = sorted(sortName, key=lambda doctor:(doctor[DOCT_NAME_IDX]))
        self.setList(sortName)
        return sortName
