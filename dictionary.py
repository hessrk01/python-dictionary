
import json
from difflib import get_close_matches as gcm


def loadFile():
    return json.load(open('data.json'))

def printJsonData(data):
    print(data)

def returnDefinition(data, key):
    key = key.lower()
    if key in data:
        return data[key]
    elif key.title() in data:
        return data[key.title()]
    elif key.upper() in data:
        return data[key.upper()]
    elif len(gcm(key, data.keys()))>0:
        answer = input("Did you mean %s instead? [Y/n]" % gcm(key, data.keys())[0])
        if answer == 'Y':
            return data[gcm(key, data.keys())[0]]
        else:
            return 'Unable to find the word'
    else:
        return 'Unable to search for the word'



data = loadFile()
#printJsonData(data)

#continue = True

#while continue:
key = input('Enter word to search for ')
definition = returnDefinition(data, key)

if type(definition) == list:
    for item in definition:
        print(item)
else:
    print(definition)
