import json

def readJSON(path: str) -> dict:
    try:
        # Opening Universities JSON file
        f = open(path)
        
        data = json.load(f)
        
        # Closing the file
        f.close()
        return data
    except:
        print("There is no json file")