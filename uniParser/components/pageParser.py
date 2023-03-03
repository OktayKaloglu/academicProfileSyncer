from concurrent.futures import ThreadPoolExecutor, wait
from multiprocessing.pool import ThreadPool
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import datetime


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

def lessonParser(url:str,instructorPath:str,lessonPath:str)->list:
    
    
    page=urlopen(Request(url=url,headers=headers))
    
    
    if page.getcode() ==200:
        soup=BeautifulSoup(page.read(),features="html.parser") 
        # todo
        # table:nth-child(12) like css selectors not working with the soup select
        # find a way to trick that
        instructors= soup.select(instructorPath)
        instructorNames=[]
        if len(instructors)>0 :
            for instructor in instructors:
                instructorNames.append(instructor.get_text(strip=True))
        
        lesson=soup.select(lessonPath)
        lessonName=""
        if len(lesson)>0:
            lessonName=lesson[0].get_text(strip=True)
        
        arr=[instructorNames,lessonName,url]
        print(datetime.datetime.now()," status: ",page.getcode(),", ",arr)
        return arr
    
    return []


def parsePage(university:dict)->list:
    
    data = []
        
    if university["initials"]!="ege" :    
        
        
        url=university["url_endpoint"]
        
        print("university: ",university["name"]," status: ",end="")
        page=urlopen(Request(url=url,headers=headers))
        print(page.getcode())
        
        if page.getcode()==200:
            soup=BeautifulSoup(page.read(),features="html.parser")
            
            rows=soup.select(university["course_href_path"])
            with ThreadPoolExecutor(max_workers=university["max_worker"]) as pool:
                results=[]
                for row in rows:
                    href=row.get("href")
                    if university["university_href_includes_domain"] :  
                        url= href 
                    else: 
                        url= university["university_prefix"]+href
                    
                    result=pool.submit(lessonParser,url,university["teacher_path"],university["lesson_name_path"])
                    results.append(result)
                wait(results)
            for res in results:
                data.append(res.result())
        
        
        
        
    
    return data
    
    """
    without multi processing
    for row in rows:
                href=row.get("href")
                if university["university_href_includes_domain"] :  
                    url= href 
                else: 
                    url= university["university_prefix"]+href
                
                data.append(lessonParser(url,university["teacher_path"],university["lesson_name_path"]))
            
    """