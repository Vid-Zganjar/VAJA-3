# Vaja 3 

**Knjiznice:**

- 'json': BUilt-in Python knjižnica za JSON 
- 'xml.etree.ElementTree':  Built-in Python knjižnica za XML 
- 'protobuf': Install via pip ('pip install protobuf')


## Serializacija in deserializacija podatkovnih struktur JSON, XML in PB

JSON (JavaScript Object Notation), XML (eXtensible Markup Language) in Protocol Buffers so tehnologije, ki se uporabljajo za shranjevanje in prenos podatkov v strukturirani obliki.

#### JSON  [dostop do vaje](https://github.com/Jabobu/Vaje_private/tree/main/JSON)

1. **Preprostost**: JSON je preprost in berljiv za ljudi, kar olajša razvoj in odpravljanje napak.
2. **Lahek**: Ker nima metapodatkov ali oznak, je JSON običajno manjši od XML, kar pomeni hitrejši prenos podatkov.
3. **Podpira osnovne tipe**: Vključuje podporo za nize, števila, logične vrednosti, matrike in objekte.
4. **Omejen tip podatkov**: Ne podpira datumov ali binarnih podatkov.
5. **Univerzalna podpora**: Široko podprt v različnih jezikih programiranja.

#### XML [dostop do vaje](https://github.com/Jabobu/Vaje_private/tree/main/XML)
1. **Razširljivost**: XML je zelo prilagodljiv in ga je mogoče prilagoditi za različne potrebe.
2. **Samoopisni**: Oznake in atributi v XML omogočajo podrobno opisovanje strukture in pomena podatkov.
3. **Podpira kompleksne tipe**: XML lahko vključuje atribute, metapodatke in celo druge XML dokumente.
4. **Težji za branje**: Zaradi metapodatkov in oznak je XML lahko bolj zapleten in težji za branje.
5. **Velikost**: Ker vključuje oznake in metapodatke, je lahko velikost datoteke večja.

#### Protocol Buffers [dostop do vaje](https://github.com/Jabobu/Vaje_private/tree/main/PB)
1. **Hitrost**: Protocol Buffers so zelo hitri za seralizacijo in deseralizacijo.
2. **Učinkovitost**: Zajemajo manj prostora kot JSON ali XML.
3. **Tipizacija**: Ponujajo močno tipizacijo, kar lahko pomaga pri odkrivanju napak.
4. **Ni berljiv za človeka**: Binarna narava Protocol Buffers pomeni, da niso berljivi brez dekodiranja.
5. **Specifična orodja**: Za delo s Protocol Buffers je potrebna uporaba posebnih orodij.

---


## Lastnosti sporočil

---
## Prevajanje med podatkovnimi strukturami

---

# Schema Translation between JSON, XML, and Protocol Buffers in Python

To perform schema translation between JSON, XML, and Protocol Buffers (PB) in Python, you can use specialized libraries for parsing and serializing these data formats. This exercise aims to provide a comprehensive guide to this translation.

## Pre-requisites:

- Basic Python Programming
- Understanding of JSON, XML, and Protocol Buffers

## Assumptions:

1. The schema types between these data formats are compatible.
2. Fields missing in one schema but present in another are either ignored or set to their default values.
3. The Protocol Buffer class `Person` is predefined and compiled from a `.proto` file.

## Explanation and Assumptions:

**Assumptions:** The assumptions about schema compatibility and how missing fields are handled are necessary because the libraries used for parsing and serialization rely on these conventions. For example, Protocol Buffers will ignore fields not present in the schema when deserializing, adhering to the assumption.

**Example Data:** Sample JSON and XML data structures were added in the code snippets to provide clear examples of how to work with these formats.

**Type Handling:** For XML to Protocol Buffers, I've added code to handle type conversion based on the attribute type in the Protocol Buffer object. This is important as XML does not inherently understand data types.


## Explanation of why the Assumptions are Needed:
 
**Schema Compatibility**: The guide assumes that the schema types between these formats are compatible. If they are not, additional mapping logic would be needed to convert between incompatible types. This assumption simplifies the guide but it's important in real-world scenarios.

**Missing Fields**: If a field is missing in one schema but present in another, it will either be ignored or set to its default value. This is a common practice to handle schema changes or differences across formats.

## Notable Improvements:

**Added Type Handling**: The improved code considers the type of the field when translating between XML and Protocol Buffers. This ensures that numerical and boolean values are handled correctly.

**Boolean Field Example**: Added an example with a boolean field in JSON to show how different types could be handled.

**Commented Protocol Buffers**: The Protocol Buffers section is commented out because it requires a .proto file and generated Python classes which can't be shown in this isolated example.


## Libraries:

1. **JSON**: Python's built-in `json` module.
2. **XML**: Python's built-in `xml.etree.ElementTree` module.
3. **Protocol Buffers**: The `protobuf` library.

## Steps:

### 1. JSON to XML

1. Use `json.loads()` to parse JSON data into a Python dictionary.
2. Create an XML root element and populate its children with key-value pairs from the dictionary.

Example:

```python
import json
import xml.etree.ElementTree as ET

# Sample JSON data
json_data = '{"name": "John", "age": 30, "is_student": false}'

# Parse JSON data
parsed_json = json.loads(json_data)

# Convert to XML
xml_root = ET.Element("person")
for key, value in parsed_json.items():
    ET.SubElement(xml_root, key).text = str(value)

# Save XML to a file
tree = ET.ElementTree(xml_root)
tree.write("person.xml")
```

### 2. JSON to Protocol Buffers

1. Use `json.loads()` to parse JSON data.
2. Use the `Parse` method from `google.protobuf.json_format` to populate a Protocol Buffer object.

Example:

```python
from google.protobuf.json_format import Parse
from example_pb2 import Person  # Assuming example_pb2 is the compiled .proto file

# Sample JSON data
json_data = '{"name": "John", "age": 30}'

# Parse JSON data to Protocol Buffer object
person_pb = Person()
Parse(json_data, person_pb)
```

### 3. XML to JSON

1. Use `ET.parse()` to read the XML file.
2. Create a Python dictionary from XML elements.
3. Use `json.dumps()` to convert the dictionary to a JSON string.

Example:

```python
# Parse XML data
xml_tree = ET.parse('person.xml')
xml_root = xml_tree.getroot()

# Convert to Python dictionary
json_dict = {child.tag: child.text for child in xml_root}

# Convert to JSON string
json_str = json.dumps(json_dict)
```

### 4. XML to Protocol Buffers

1. Use `ET.parse()` to read the XML file.
2. Populate the Protocol Buffer object with the XML elements.

Example:

```python
# Sample Protocol Buffer object
person_pb = Person()

# Populate Protocol Buffer object
for child in xml_root:
    attr_type = type(getattr(person_pb, child.tag, None))
    value = int(child.text) if attr_type is int else child.text
    setattr(person_pb, child.tag, value)
```

### 5. Protocol Buffers to JSON

1. Use `MessageToJson` from `google.protobuf.json_format` to serialize the Protocol Buffer object to a JSON string.

Example:

```python
from google.protobuf.json_format import MessageToJson

# Convert Protocol Buffer object to JSON string
json_str = MessageToJson(person_pb)
```
