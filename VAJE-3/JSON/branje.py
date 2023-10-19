import json

with open(r'/Users/Vid/Desktop/TP VAJE/VAJA3/VAJE/VAJE-3/JSON/pisanje.py','r') as f:
    deserialized_person=json.load(f)

deserialized_person['starost']=40
deserialized_person['porocen']=True

with open(r'/Users/Vid/Desktop/TP VAJE/VAJA3/VAJE/VAJE-3/JSON/pisanje.py','w') as f:
    json.dump(deserialized_person, f, indent=4)
