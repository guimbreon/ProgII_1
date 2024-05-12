#-*- coding: utf-8 -*-

# 2023-2024 Programação 2 (LTI)
# Grupo 13
#62372 Guilherme Soares
#62242 Adriano Neves
"""from Doctors import Doctors

data = [['Guilherme Gaspar', '2', 'weekly leave', '60', [40, 10]], ['Horácio Horta', '3', [14, 50], '140', [7, 40]], ['Ildefonso Inácio', '2', 'weekly leave', '60', [40, 10]], ['José Justo', '2', [14, 50], '60', [15, 20]]]

doctor = Doctors(data[1])
print(doctor.getTime(),doctor.getMins())

doctor.add20Min()

print(doctor.getTime(),doctor.getMins())

"""

# Example usage:
#Windows:
#filePath = ""
#linux

#doctors
filePathDoc = ""
fileDoc = FileHandling(filePathDoc)
fileDoc.readFile()
doctors = fileDoc.getList()
headerDoc = fileDoc.getHeader()


#mothers aka requests
filePathMoth = ""
fileMoth = FileHandling(filePathMoth)
fileMoth.readFile()
mothers = fileMoth.getList()
headerMoth = fileMoth.getHeader()


#schedule
filePathSch = ""
fileSch = FileHandling(filePathSch)
fileSch.readFile()
schedules = fileSch.getList()
headerSch = fileSch.getHeader()

"""
doctors = Lists(doctors)
for item in doctors.getList():
    print(item)
    item.add20Min()


print("\n add20Min")
doctors = doctors.getList()
for item in doctors:
    print(item.getDoctor())

print("\n order")
doctors = Lists(doctors)

doctors = doctors.sortDoctor()
for item in doctors:
    print(item)"""



"""mothers = Lists(mothers)
mothers = mothers.sortMothers()
for mother in mothers:
    print(mother)"""

"""schedules= Lists(schedules)


schedules = schedules.sortSchedule()
for schedule in schedules:
    print(schedule)"""



"""
Update birth assistance schedule assigning the given birth assistance requested
to the given doctors, taking into account a previous schedule.

Requires:
doctors is a list of lists with the structure as in the output of
infoFromFiles.readDoctorsFile concerning the time of previous schedule;
requests is a list of lists with the structure as in the output of 
infoFromFile.readRequestsFile concerning the current update time;
previousSched is a list of lists with the structure as in the output of
infoFromFiles.readScheduleFile concerning the previous update time;
nextTime is a string in the format HHhMM with the time of the next schedule
Ensures:
a list of birth assistances, representing the schedule updated at
the current update time (= previous update time + 30 minutes),
assigned according to the conditions indicated in the general specification
of the project (omitted here for the sake of readability) and
a list of doctors with their times updated after being sorted for a given birth.
"""
time = DateTime(headerMoth[REQ_HEADER][REQ_HEADER_TIME])


"""for schedled in schedules:
    print(schedled)"""

"""
VER SE OS SORTINGS ESTÃO A FUNCIONAR MESMO

"""


mothers = Lists(mothers)
mothers.sortMothers()

schedules= Lists(schedules)
schedules.sortSchedule()
doctors = Lists(doctors)
doctors.sortDoctor()

newSched, newDocs = schedules.updateSchedule(doctors.getList(), mothers.getList(), schedules.getList(), time.hourToList())
for item in newSched:
    print(item)

for item in newDocs:
    print(item)

hour = headerDoc[1].pop(3)
hour = [int(hour[0:2]),int(hour[3:5])]
hour[1] += 30
if hour[1] >= 60:
    hour[0] +=1
    hour[1] = "00"
headerDoc[1].insert(3, f"{hour[0]}h{hour[1]}\n")
writing = InfoToFile(headerDoc[1], headerSch[1], newDocs, newSched, "", "")

writing.writeDocFile()

print("\n\n\n\n")
writing.writeSchedFile()



