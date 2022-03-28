import json

def readJsonFile(filename):
    data=""
    try:
        with open("/home/ec2-user/environment/python6/insulin.json") as json_file:
            data = json.load(json_file)
            #print(data)
    except IOError:
        print("Could not read file")
    return data
    
