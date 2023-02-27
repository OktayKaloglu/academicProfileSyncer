from urllib.request import urlopen
from bs4 import BeautifulSoup

def getInstructorName(url:str,path:str)->str:
    
    page=urlopen(url)
    soup=BeautifulSoup(page.read())
    name = soup.select(path)
    #todo soup returns html element .text is not working to get the string find a way
    return name



def parsePage(university:dict)->list:
    if university["initials"]=="iyte" :    
        url=university["url_endpoint"]
        page=urlopen(url)
        
        
        soup=BeautifulSoup(page.read(),features="html.parser")
        
        data = []
        table = soup.find('table')
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele]) # Get rid of empty values
                
        
        
        #getInstructorName()
        
    
    return []