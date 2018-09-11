import os
import json

def load(filename):
    dir = os.path.dirname(__file__)
    file_path = os.path.join(dir, ('%s' % filename))
    with open(file_path, 'r') as schema_file:
        data = json.load(schema_file)
    #print(data)    
    return data
