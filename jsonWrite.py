import json

def writeJson(arr:list,path:str)->None:
    json_object = json.dumps(arr,ensure_ascii=False, indent=4)
    with open(path, "w",encoding="UTF-8") as outfile:
        outfile.write(json_object)