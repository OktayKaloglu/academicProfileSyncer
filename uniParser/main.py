from asyncio import sleep
from datetime import datetime
from multiprocessing import Pool
from components.readConfig import readJSON
from components.pageParser import parsePage
import csv


def writeCsv(arr,file):
    with open(file, 'w', newline='') as csv_file:
     writer = csv.writer(csv_file)
     for row in arr:
         writer.writerow(row)
    csv_file.close()
    
def readCsv(path):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')
    csv_file.close()

# get all the universities from the universities file
universities=readJSON('universities.json')



parsedData=[]
# Iterating through the Universities
time=datetime.now()

for university in universities['universities']:
    parsedData.append(parsePage(university))


time2=datetime.now()
sleep(27)
print(parsedData)
print("time takes: ",time2-time)