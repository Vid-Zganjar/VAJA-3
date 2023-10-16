# Vaja 3 - Serializacija sporočil z JSON,XML in PB

V vaji bomo z python serilizirali, deserializirali sporočila POPRAVI

**Knjiznice:**

- 'json': BUilt-in Python knjižnica za JSON 
- 'xml.etree.ElementTree':  Built-in Python knjižnica za XML 
- 'protobuf': Install via pip ('pip install protobuf')


## Serializacija in deserializacija podatkovnih struktur JSON, XML in PB

JSON (JavaScript Object Notation), XML (eXtensible Markup Language) in Protocol Buffers so tehnologije, ki se uporabljajo za shranjevanje in prenos podatkov v strukturirani obliki.

#### JSON  [dostop do vaje JSON](https://github.com/Jabobu/Vaje_private/tree/main/JSON)

1. **Preprostost**: JSON je preprost in berljiv za ljudi, kar olajša razvoj in odpravljanje napak.
2. **Lahek**: Ker nima metapodatkov ali oznak, je JSON običajno manjši od XML, kar pomeni hitrejši prenos podatkov.
3. **Podpira osnovne tipe**: Vključuje podporo za nize, števila, logične vrednosti, matrike in objekte.
4. **Omejen tip podatkov**: Ne podpira datumov ali binarnih podatkov.
5. **Univerzalna podpora**: Široko podprt v različnih jezikih programiranja.

#### XML [dostop do vaje XML](https://github.com/Jabobu/Vaje_private/tree/main/XML)
1. **Razširljivost**: XML je zelo prilagodljiv in ga je mogoče prilagoditi za različne potrebe.
2. **Samoopisni**: Oznake in atributi v XML omogočajo podrobno opisovanje strukture in pomena podatkov.
3. **Podpira kompleksne tipe**: XML lahko vključuje atribute, metapodatke in celo druge XML dokumente.
4. **Težji za branje**: Zaradi metapodatkov in oznak je XML lahko bolj zapleten in težji za branje.
5. **Velikost**: Ker vključuje oznake in metapodatke, je lahko velikost datoteke večja.

#### Protocol Buffers [dostop do vaje PB](https://github.com/Jabobu/Vaje_private/tree/main/PB)
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

