""" module that validates the license plate considering the cnf file """
import json

#cnf: the cnf json file
#plate: the plate string

def validate_plates(cnf, plate):
    # open the cnf json
    with open(cnf) as f:
        cnf = json.load(f)

    if(checklength(cnf, plate) and checkletters(cnf, plate) and checknumbers(cnf, plate)):
        return True
    else:
        return False
    
def checklength(cnf, plate):
    if(cnf['length'] == len(plate)):
        return True
    return False

def checkletters(cnf, plate):
    letters = []
    for char in plate:
        if char.isalpha():
            letters.append(char)
    return len(letters) == cnf['letters']
    
def checknumbers(cnf, plate):
    numbers = []
    for char in plate:
        if char.isdigit():
            numbers.append(char)
    return len(numbers) == cnf['numbers']

cnf = input("cnf file:")
plate = input("Plate:")
print(validate_plates(cnf, plate))
