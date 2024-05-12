#-*- coding: utf-8 -*-

# 2023-2024 Programação 2 (LTI)
# Grupo 13
#62372 Guilherme Soares
#62242 Adriano Neves
from constants import *
from DateTime import DateTime
from Doctors import Doctors
from Mother import Mother
from Schedule import Schedule

class FileHandling:
    """
    A class for handling file operations and data parsing.

    Attributes:
        _fileName (str): The path to the file.
        _Header (list): A list to store the header information.
        _List (list): A list to store data read from the file.

    Methods:
        __init__(self, fileName): Initializes a FileHandling object.
        __str__(self): Returns the path of the file.
        getHeader(self): Getter method for retrieving the header information.
        setHeader(self, header): Setter method for setting the header information.
        getList(self): Getter method for retrieving the data list.
        setList(self, list): Setter method for setting the data list.
        readFile(self): Reads the file and parses its contents.
    """

    def __init__(self, fileName):
        """
        Initializes a FileHandling object.

        Args:
            fileName (str): The path to the file.

        Attributes:
            _fileName (str): The path to the file.
            _Header (list): A list to store the header information.
            _List (list): A list to store data read from the file.
        """
        self._fileName = fileName
        self._Header = []
        self._List = [] 

    def __str__(self) :
        """
        Returns the path of the file.

        Returns:
            str: The path of the file.
        """
        return self._fileName
    
    def getHeader(self):
        """
        Getter method for retrieving the header information.

        Returns:
            list: The header information.
        """
        return self._Header

    def setHeader(self, header):
        """
        Setter method for setting the header information.

        Args:
            header (list): The header information to be set.
        """
        self._Header = header

    def getList(self):
        """
        Getter method for retrieving the data list.

        Returns:
            list: The data list.
        """
        return self._List

    def setList(self, list):
        """
        Setter method for setting the data list.

        Args:
            list (list): The data list to be set.
        """
        self._List = list


    def readFile(self):
        """
        Reads the file and parses its contents.

        Reads a given file and turns it into a collection and its type (Requests, Doctors, or Schedule).

        Returns:
            tuple: A tuple containing two elements:
                - list of lists: Each list corresponds to the data from each line in the file.
                - list: Information about the type of file being read.
        """
        fileData = open(self.__str__(), "r")
        newList = []
        fileInfo = []
        header = []
        lineNum = 0
        for line in fileData:
            if lineNum <= 6:
                header.append(line)
            if lineNum == 6:
                fileInfo.append(line.rstrip())
            if lineNum > 6 and len(line.split()) != 0:
                newLine = line.rstrip().split(", ")
                finalLine = []
                for item in newLine:
                    if "h" in item and item[0].isdigit(): #it separates hours and minutes into a list
                        timeList =[]
                        timeList.append(DateTime.hourToInt(item))
                        timeList.append(DateTime.minutesToInt(item))
                        finalLine.append(timeList)
                    else:
                        finalLine.append(item)
                if fileInfo[0] == "Doctors:":
                    newList.append(Doctors(finalLine))
                elif fileInfo[0] == "Mothers:":
                    newList.append(Mother(finalLine))
                elif fileInfo[0] == "Schedule:":
                    newList.append(Schedule(finalLine))
            lineNum += 1
        fileData.close()
        fileInfo.append(header)
        self.setList(newList)
        self.setHeader(fileInfo)

