import person_pb2
person = person_pb2.Person()

with open(r"C:\Users\Vid\Desktop\TP VAJE\VAJA3\VAJE\VAJE-3\DATA\POMOC\person.pb","rb") as f:
    person.ParseFromString(f.read())

person.age=31
person.married=False

with open(r"C:\Users\Vid\Desktop\TP VAJE\VAJA3\VAJE\VAJE-3\DATA\POMOC\person_updated.pb","wb") as f:
    f.write(person.SerializeToString())

print(person)