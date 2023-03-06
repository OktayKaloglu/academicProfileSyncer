from asyncio import sleep
from datetime import datetime
from multiprocessing import Pool
from components.readConfig import readJSON
from components.pageParser import parsePage
import csv


def writeCsv(arr,file):
    with open(file, 'w', newline='') as csv_file:
     writer = csv.writer(csv_file)
     for uni in parsedData:
        #an error occurs by the ege uni.
        # teachers line has /n init 
        for row in uni:
            if "\n" in row[0]:
                row[0]= row[0].split("\n")
            for teacher in row[0]:
                writer.writerow([teacher,row[1],row[2]])
    csv_file.close()
    


# get all the universities from the universities file
universities=readJSON('universities.json')



parsedData=[]
# Iterating through the Universities
time=datetime.now()

for university in universities['universities']:
    parsedData.append(parsePage(university))



sleep(27)
#print(parsedData)

writeCsv(parsedData,"teachers.csv")
time2=datetime.now()
print("time takes: ",time2-time)