import person_pb2

person =person_pb2.Person()

person.name="Lojze"
person.age=30
person.street="Titova"
person.city="ljubljana"
person.married=True

with open(r"C:\Users\Vid\Desktop\TP VAJE\VAJA3\VAJE\VAJE-3\DATA\POMOC\person.pb", 'wb') as f:
    f.write(person.SerializeToString())
