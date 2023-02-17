import requests
import json
from pprint import pprint as pp


pp("Encoding Python objects into JSON:")
print()
encode_obj = json.dumps({
            "ID Nation": "01000US",
            "Nation": "United States",
            "ID Year": 2019,
            "Year": "2019",
            "Population": 324697795,
            "Slug Nation": "united-states"
})
print()

pp('Decoding the Python object into JSON: ')
decode_obj = json.loads(encode_obj)
pp(decode_obj)
print()

with open('conversionrate.json','r') as f:
    show_jsonfile = json.loads(f.read())
print()

pp('Show the type of the Python')
pp(type(show_jsonfile))
print()

pp('Read JSON file into the Python object:')
pp(show_jsonfile)
print()

pp('Parse out the json file')
print()

print("The ID Nation is: ") 
pp(show_jsonfile['data'][0]['ID Nation'])
print()
print("The Id Year is: ")
pp(show_jsonfile['data'][3]['ID Year'])
print()

print()
pp(show_jsonfile['source'][0]['annotations'])