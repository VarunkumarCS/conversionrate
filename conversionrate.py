import requests
import json
from json import JSONDecodeError
from pprint import pprint as pp

def main():
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

    #reading the json file in the try-exception block
    try:
        with open('conversionrate.json','r') as f:
            show_jsonfile = json.loads(f.read())
    except JSONDecodeError as error:
        print("JSON Decoding Error: ")
        print(error.msg)
        print("The error line number is : ",error.lineno)
        print("The column number is:", error.colno)
    print()

    #Printing the json data in the string
   
    print("Dumping the JSON Data:")
    jsonStr = json.dumps(show_jsonfile)
    print(jsonStr)
    print()

    #showing the data type of the json file
    pp('Show the type of the Python')
    pp(type(show_jsonfile))
    print()

    #opening the json file in the terminal
    pp('Read JSON file into the Python object:')
    pp(show_jsonfile)
    print()

    #PARSING THE JSON FILE
    pp('Parse out the json file')
    print()

    #printing the data
    try:
        population = show_jsonfile['data'][0]['Population']
        pp(("The population in 2022 is:", population))
    except JSONDecodeError as error2:
        print("JSON DATA decoding error:")
        print(error2.msg)
        print("The error line number is : ", error2.lineno)
        print("The column number is:", error2.colno)
    print()

    id_year = show_jsonfile['data'][3]['ID Year']
    pp(("The ID Year is:", id_year))
    print()

    #Data is present in the JSON file
    if (show_jsonfile['source']):
        print("The data from source attribute is present")
        print()
        pp(show_jsonfile['source'][0]['annotations'])
    else:
        print("The data from source attributes is not present")


if __name__ == "__main__":
    main()


