from scholarly import ProxyGenerator,scholarly
from jsonWrite import writeJson
from concurrent.futures import ThreadPoolExecutor,wait
import time

time1=time.time()
# Set up a ProxyGenerator object to use free proxies
# This needs to be done only once per session
pg = ProxyGenerator()
pg.FreeProxies()
scholarly.use_proxy(pg)


# Retrieve the author's data, fill-in, and print
search_query = scholarly.search_author('Murat Osman ÜNALIR')

author = scholarly.fill(next(search_query))

def getPaper(pub):
    #pubs.append(scholarly.fill(pub))
    print(pub["bib"]["title"])
    
    scholarly.fill(pub)


with ThreadPoolExecutor(max_workers=150) as pool:
    for pub in author['publications']:
        
        if(not pg._check_proxy(pg)):
            
            #todo
            #there is a case that after all the free proxies cycled trough algorithm will stuck at the loop for some time.
            #need to implement a solution like check the pg health if dead create a new pg
            #creating a new pg for every iteration will take to much time 
            pg.get_next_proxy()
            scholarly.use_proxy(pg)
            
        pool.submit(getPaper,pub)
        
    

time2=time.time()
    
filled=0
total=len(author['publications'])
for pub in author['publications']:
    if pub["filled"] :
        filled+=1
        
print ("total: ",total)
print("filled: ",filled)
print("diff: ",total-filled)

print("time it takes: ",time2-time1)

writeJson(author,"MuratOsmanÜnalir.json")