import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

# convert a python dict into a json file

my_family = {
    "parents":["Beth", "Jerry"],
    "children" : ["Summer", "Morty"]
}

with open(dir_path + '/my_family.json', 'w') as f:
    json.dump(my_family, f) #dumps is for string


# convert a python dict into a json string (short data)
my_family_json = json.dumps(my_family)
print(my_family_json)
print(type(my_family_json)) #string

# convert a json file into a python dict
with open(dir_path + '/my_family.json', 'r') as f:
    my_family2 = json.load(f) #loads is for json string into a dict

print(my_family2)
print(type(my_family2)) #dict 

# convert a json string into a python dict
my_family3 = json.loads(my_family_json)
print(my_family3)
print(type(my_family3)) #dict