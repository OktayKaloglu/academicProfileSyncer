from components.readConfig import readJSON
from components.pageParser import parsePage
# get all the universities from the universities file
universities=readJSON('universities.json')

#todo create an university type

collectedData=[]

# Iterating through the Universities
for university in universities['universities']:
    collectedData.append(parsePage(university))
    
print(collectedData)