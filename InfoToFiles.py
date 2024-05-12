#-*- coding: utf-8 -*-

# 2023-2024 Programação 2 (LTI)
# Grupo 13
#62372 Guilherme Soares
#62242 Adriano Neves
from FileHandling import FileHandling
from DateTime import DateTime
from Doctors import Doctors
from constants import *

class InfoToFile:
    """
    Class to handle writing information to files.
    """

    def __init__(self, headerDoc, headerSched, doclist, schedlist, fileNameSchd, fileNameDoc):
        """
        Initialize InfoToFile object.

        Args:
        - headerDoc (list): List of strings representing the header for doctor information.
        - headerSched (list): List of strings representing the header for schedule information.
        - doclist (list): List of lists containing doctor information.
        - schedlist (list): List of DateTime objects containing schedule information.
        - fileNameSchd (str): Name of the file to write schedule information to.
        - fileNameDoc (str): Name of the file to write doctor information to.
        """
        self._headerSched = headerSched
        self._headerDoc = headerDoc
        self._doclist = doclist
        self._fileNameDoc = fileNameDoc
        self._fileNameSchd = fileNameSchd
        self._schedlist = schedlist

    def getSchedList(self):
        """
        Get the schedule list.

        Returns:
        - list: Schedule list.
        """
        return self._schedlist
        
    def getHeader(self):
        """
        Get the header.

        Returns:
        - str: Header.
        """
        return self._header

    def getDocList(self):
        """
        Get the doctor list.

        Returns:
        - list: Doctor list.
        """
        return self._doclist

    def getFileName(self):
        """
        Get the file name.

        Returns:
        - str: File name.
        """
        return self._fileName

    def setSchedList(self, SchedL):
        """
        Set the schedule list.

        Args:
        - SchedL (list): Schedule list.
        """
        self._schedlist = SchedL

    def setHeader(self, Header):
        """
        Set the header.

        Args:
        - Header (str): Header.
        """
        self._header = Header

    def setDocList(self, List):
        """
        Set the doctor list.

        Args:
        - List (list): Doctor list.
        """
        self._doclist = List

    def setFileName(self, FileName):
        """
        Set the file name.

        Args:
        - FileName (str): File name.
        """
        self._fileName = FileName

    def __str__(self):
        """
        String representation of the object.

        Returns:
        - str: String representation.
        """
        return "Header: " + str(self._header) + "\nList: " + str(self._list) + "\nFileName: " + str(self._fileName)
        
    def writeDocFile(self):
        """
        Write doctor information to a file.
        """
        count = 0
        fp = open(self._fileNameDoc, 'w')
        for line in self._headerDoc:
            fp.write(line)
        for item in self._doclist:
            count += 1
            if count != len(self._doclist):
                if item[DOCT_TIME_IDX] == "weekly leave":
                    fp.write(f"{item[DOCT_NAME_IDX]}, {item[DOCT_CAT_IDX]}, {item[DOCT_TIME_IDX]}, {item[DOCT_MINS_IDX]}, {item[DOCT_TOTALTIME_IDX][0]}h{item[DOCT_TOTALTIME_IDX][1]}\n")
                else:
                    fp.write(f"{item[DOCT_NAME_IDX]}, {item[DOCT_CAT_IDX]}, {item[DOCT_TIME_IDX][0]}h{item[DOCT_TIME_IDX][1]}, {item[DOCT_MINS_IDX]}, {item[DOCT_TOTALTIME_IDX][0]}h{item[DOCT_TOTALTIME_IDX][1]}\n")
            else:
                if item[DOCT_TIME_IDX] == "weekly leave":
                    fp.write(f"{item[DOCT_NAME_IDX]}, {item[DOCT_CAT_IDX]}, {item[DOCT_TIME_IDX]}, {item[DOCT_MINS_IDX]}, {item[DOCT_TOTALTIME_IDX][0]}h{item[DOCT_TOTALTIME_IDX][1]}")
                else:
                    fp.write(f"{item[DOCT_NAME_IDX]}, {item[DOCT_CAT_IDX]}, {item[DOCT_TIME_IDX][0]}h{item[DOCT_TIME_IDX][1]}, {item[DOCT_MINS_IDX]}, {item[DOCT_TOTALTIME_IDX][0]}h{item[DOCT_TOTALTIME_IDX][1]}")
        fp.close()
    
    def writeSchedFile(self):
        """
        Write schedule information to a file.
        """
        count = 0
        fp = open(self._fileNameSchd, "w")
        for line in self._headerSched:
            fp.write(line)
        for item in self._schedlist:
            count += 1
            item = item.getSchd()
            if count != len(self._schedlist):
                fp.write(f"{item[REQ_TIME_IDX][0]}h{item[REQ_TIME_IDX][1]}, {item[REQ_MOTH_IDX]}, {item[REQ_DOC_IDX]}\n")
            else:
                fp.write(f"{item[REQ_TIME_IDX][0]}h{item[REQ_TIME_IDX][1]}, {item[REQ_MOTH_IDX]}, {item[REQ_DOC_IDX]}")
        fp.close()
