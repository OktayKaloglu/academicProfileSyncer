import openai

from jsonWrite import writeJson 
from components.readConfig import readJSON


openai.api_key = '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'



def generate_text(prompt):
    completion = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo-0301',
    max_tokens=3990,
    messages = [ 
    {'role': 'user', 'content': prompt}
    ],

    temperature = 1.2    
    )
    return completion['choices'][0]['message']['content']


    
ders="Write a ten thousand word essay that Industry 4.0's impact on the business management"



with open('readme.txt', 'w') as f:
    f.write(generate_text(ders))