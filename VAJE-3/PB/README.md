## PB

Protocol Buffers (PB) je binarna serializacijska oblika. Za razliko od človeku berljivih formatov, kot sta JSON in XML, so PB-ji  učinkovitejši, vendar zahtevajo vnaprej določeno shemo. Shema, običajno definirana v datotekah `.proto`, določa strukturo podatkov, zaradi česar je nevtralna glede platforme in jezika. Te datoteke `.proto` so uporabljene pri "ustvarjanje" kode v jezikih, kot je Python, ki se nato  uporabi za serializacijo in deserializacijo podatkov.

### Razlaga elementov PB
1. **Sporočilo**: Osnovna enota v PB-jih, podobna objektu ali strukturi (ang. strcut) v mnogih programskih jezikih.
2. **Polje**: Vsako sporočilo lahko vsebuje eno ali več polj z določeno vrsto (npr. `int32`, `string`, `bool`) in edinstvenim identifikatorjem.
3. **Enumeratorji/naštevniki**: Omogočajo definiranje vrste z vnaprej določenimi konstantnimi vrednostmi.
4. **Gnezdenje**: Sporočila in naštevanja lahko ugnezdite znotraj drugih sporočil za organizacijske namene.

#### Primeri

1. **Preprosto sporočilo**
    ```protobuf
    message Person {
      string name = 1;
      int32 age = 2;
    }
    ```

2. **Sporočilo z enumeratrojem**
    ```protobuf
    message Student {
      enum Grade {
        FRESHMAN = 0;
        SOPHOMORE = 1;
        JUNIOR = 2;
        SENIOR = 3;
      }
      string name = 1;
      Grade grade = 2;
    }
    ```

3. **Gnezdenje**
    ```protobuf
    message Family {
      message Member {
        string name = 1;
        int32 age = 2;
      }
      repeated Member members = 1;
    }
    ```

---

Knjižnica Python Protocol Buffers, `protobuf`, ponuja funkcije, podobne Pythonovi knjižnici `json` za branje in pisanje podatkov PB.

### PB operacije z uporabo Pythonove knjižnice `protobuf`

1. **Serializacija**: Pretvarjanje objektov Python v binarno obliko PB
     - `SerializeToString()`: Serializira sporočilo in ga vrne kot niz.
  
2. **Deserializacija**: pretvorba binarnega formata PB nazaj v objekte Python
     - `ParseFromString(data)`: razčleni sporočilo iz podanega niza.
  
---

#### Vaja: Serializiraj, deserializiraj in manipuliraj s podatki PB

Najprej boste potrebovali datoteko `.proto`, da definirate shemo. Ustvarite na primer datoteko `person.proto` z naslednjo vsebino:

```protobuf
syntax = "proto3";
message Person {
  string name = 1;
  int32 age = 2;
  string street = 3;
  string city = 4;
  bool married = 5;
}
```

Prevedite (ang. compile) to datoteko `.proto` s PB prevajalnikom  (`protoc`), da ustvarite kodo Python:

```bash
protoc --python_out=. person.proto
```

To bo ustvarilo datoteko `person_pb2.py`, ki vsebuje pythonove razrede (ang. classes) vnos podatkov.

##### Serializacija PB datoteke


```python
import person_pb2

# Create a Person object and set fields
person = person_pb2.Person()
person.name = "Alice"
person.age = 30
person.street = "Dunajska"
person.city = "Ljubljana"
person.married = True

# Serialize to file
with open("./person.pb", "wb") as f:
    f.write(person.SerializeToString())
```

##### Deserializacija PB datoteke

```python
# Create an empty Person object
person = person_pb2.Person()

# Deserialize from file
with open("./person.pb", "rb") as f:
    person.ParseFromString(f.read())

# Manipulate the data (e.g., change age and married status)
person.age = 31
person.married = False

# Serialize back to file
with open("./person_updated.pb", "wb") as f:
    f.write(person.SerializeToString())
```
