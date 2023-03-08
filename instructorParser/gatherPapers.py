from scholarly import ProxyGenerator,scholarly
from jsonWrite import writeJson
from concurrent.futures import ThreadPoolExecutor,wait
# Set up a ProxyGenerator object to use free proxies
# This needs to be done only once per session
pg = ProxyGenerator()
pg.FreeProxies()
scholarly.use_proxy(pg)


# Retrieve the author's data, fill-in, and print
search_query = scholarly.search_author('Murat Osman ÜNALIR')
author = scholarly.fill(next(search_query))

pubs=[]

with ThreadPoolExecutor(max_workers=1000) as pool:
    results=[]
    for pub in author['publications']:
        #pubs.append(scholarly.fill(pub))
        print(pub["bib"]["title"])
        result=pool.submit(scholarly.fill,pub)
        results.append(result)
    wait(results)
    for res in results:
        pubs.append(res)


writeJson(pubs,"MuratOsmanÜnalir.json")

"""
# Print the titles of the author's publications
print([pub['bib']['title'] for pub in author['publications']])

# Take a closer look at the first publication
pub = scholarly.fill(author['publications'][0])
print(pub)

# Which papers cited that publication?
print([citation['bib']['title'] for citation in scholarly.citedby(pub)])
"""