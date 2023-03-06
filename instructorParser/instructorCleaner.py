#todo 
#an error occurs ModuleNotFoundError: No module named 'uniParser'
"""
from uniParser.main import parseLessons 
parseLessons()
"""


import pandas as pd
from jsonWrite import writeJson    

def print_full(x):
    pd.set_option('display.max_rows', len(x))
    print(x)
    pd.reset_option('display.max_rows')

def split_instructors(x):
    
    for sep in [',','\n']:
        if sep in x:
            x=x.split(sep)
            repX=[]
            for item in x:
                if len(item)>0:
                    if not str.isdigit(item[0]) :
                        repX.append(item)      
            #new list could contain more than 1 instructor
            x=repX
            # if list contains just one instructor
            if len(repX)==1:
                
                x=repX[0]
    return x


instructors=pd.read_csv("teachers.csv",sep=',',names=["instructor","lesson","url"])
instructors.dropna(axis="index",inplace=True)
#convert str the instructor column for further split operations
instructors.instructor = instructors.instructor.astype(str)
instructors["instructor"]=instructors["instructor"].apply(lambda x:split_instructors(x))
instructors=instructors.explode('instructor')
instructors["instructor"]=instructors["instructor"].apply(lambda x: x.strip())
instructors=instructors["instructor"].unique().tolist()

writeJson(instructors,"cleaned_instructor.json")
