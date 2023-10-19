import os
import json
from person_pb2 import Person

file_size = os.path.getsize(r"C:\Users\Vid\Desktop\TP VAJE\VAJA3\VAJE\VAJE-3\DATA\POMOC\person.json")
print(f"JSON file size: {file_size} bytes")

file_size=os.path.getsize(r"C:\Users\Vid\Desktop\TP VAJE\VAJA3\VAJE\VAJE-3\DATA\POMOC\person.pb")
print(f"PB file size:  {file_size} bytes")

with open(r"C:\Users\Vid\Desktop\TP VAJE\VAJA3\VAJE\VAJE-3\DATA\POMOC\person.json","r") as f:
    data=json.load(f)

for key,value in data.items():
    print(f"{key}:{type(value)}")



person_pb = Person()

with open(r'C:\Users\Vid\Desktop\TP VAJE\VAJA3\VAJE\VAJE-3\DATA\POMOC\person.pb', 'rb') as f:
    person_pb.ParseFromString(f.read())


for field, value in person_pb.ListFields():
    print(f"Field: {field.name}, Type: {field.type}, Value: {value}")