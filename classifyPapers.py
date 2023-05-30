
import time
import openai

from jsonWrite import writeJson 
from components.readConfig import readJSON


openai.api_key = ''



def generate_text(prompt):
    completion = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [ 
    {'role': 'user', 'content': prompt}
    ],
    temperature = 0    
    )
    return completion['choices'][0]['message']['content']

def ask(prompt):
    for i in range(10):
        try:
            response= generate_text(prompt)
            return response
        except:
            time.sleep(10)

    return "failed"

    

related=[]
author=readJSON("MuratOsmanÜnalir.json")
pubs=author["publications"]
for pub in pubs:
    if pub["filled"]:
        #print(pub["bib"]["abstract"])
        try:
            prompt = "Do not explain the response, What is the most related 5 computer science courses to following abstract, add how close they are with percentage. "+pub['bib']['abstract']        
            #print(pub['bib']['abstract'])
        except:
            continue
        response=ask(prompt)

        arr=[]
        temp=response.split('\n')
        for line in temp:
            arr.append([line[3:-6],line[-4:-2]])
        #cities_id,course_name,percentage
        related.append([pub['author_pub_id'],arr])
        print(related)
        

writeJson(related,"related.json")