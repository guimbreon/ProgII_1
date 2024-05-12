#-*- coding: utf-8 -*-

# 2023-2024 Programação 2 (LTI)
# Grupo 13
#62372 Guilherme Soares
#62242 Adriano Neves
from FileHandling import FileHandling
from Doctors import Doctors
from Lists import Lists 
import sys
from constants import *

from InfoToFiles import InfoToFile
from DateTime import DateTime

def errorHandling(fileInfo, expected, fileName):
    """
    Handles the error if the file given is not of the expected type.

    Args:
        fileInfo (str): The header information extracted from the file.
        expected (str): The expected header information.
        fileName (str): The name of the file being processed.

    Raises:
        IOError: If there is a scope inconsistency between the name and header in the file.
    """
    if fileInfo == expected:
        pass
    else:
        raise IOError(f"\n\nFile head error: scope inconsistency between name and header in file {fileName}.")

def plan(filePathDoc, filePathSch, filePathMoth):
    """
    Runs the birthPlan application.

    Args:
        filePathDoc (str): The path to the file containing the list of doctors.
        filePathSch (str): The path to the file containing the list of birth assistances.
        filePathMoth (str): The path to the file containing the list of mothers.

    Ensures:
        Writing of two .txt files containing the updated list of doctors assigned
        to mothers and the updated list of birth assistances, according to 
        the requirements in the general specifications provided (omitted here for 
        the sake of readability);
        these two output files are named, respectively, doctorsXXhYY.txt and
        scheduleXXhYY.txt, where XXhYY represents the time 30 minutes
        after the time t indicated in the files doctorsFileName,
        scheduleFileName and requestsFileName, and are written in the same directory
        of the latter.
    """
    # Doctors
    fileDoc = FileHandling(filePathDoc)
    fileDoc.readFile()
    doctors = fileDoc.getList()
    headerDoc = fileDoc.getHeader()
    errorHandling(headerDoc[0], "Doctors:", filePathDoc)

    # Mothers (requests)
    fileMoth = FileHandling(filePathMoth)
    fileMoth.readFile()
    mothers = fileMoth.getList()
    headerMoth = fileMoth.getHeader()
    errorHandling(headerMoth[0], "Mothers:", filePathMoth)

    # Schedule
    fileSch = FileHandling(filePathSch)
    fileSch.readFile()
    schedules = fileSch.getList()
    headerSch = fileSch.getHeader()
    errorHandling(headerSch[0], "Schedule:", filePathSch)

    time = DateTime(headerMoth[REQ_HEADER][REQ_HEADER_TIME])

    mothers = Lists(mothers)
    mothers.sortMothers()

    schedules = Lists(schedules)
    schedules.sortSchedule()
    doctors = Lists(doctors)
    doctors.sortDoctor()

    newSched, newDocs = schedules.updateSchedule(doctors.getList(), mothers.getList(), schedules.getList(), time.hourToList())

    oldHour = headerDoc[1][3].replace("\n","")

    hour = headerDoc[1].pop(3)
    t = headerSch[1].pop(3)
    hour = [int(hour[0:2]), int(hour[3:5])]
    hour[1] += 30
    if hour[1] >= 60:
        hour[0] += 1
        hour[1] = "00"
    headerDoc[1].insert(3, f"{hour[0]}h{hour[1]}\n") 
    headerSch[1].insert(3, f"{hour[0]}h{hour[1]}\n") 

    intoSchd = filePathSch.replace(oldHour, f"{hour[0]}h{hour[1]}")
    intoDoc = filePathDoc.replace(oldHour, f"{hour[0]}h{hour[1]}")

    writing = InfoToFile(headerDoc[1], headerSch[1], newDocs, newSched, intoSchd, intoDoc)

    writing.writeSchedFile()
    writing.writeDocFile()

plan(sys.argv[1],sys.argv[2],sys.argv[3])
