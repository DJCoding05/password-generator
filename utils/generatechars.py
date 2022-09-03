from string import digits, ascii_lowercase, ascii_uppercase


def generateCharacters(useSymbols=False, useNumbers=False, useLowerCase=False, useUpperCase=False):
    listOfCharacters = []
    if useSymbols:
        listOfCharacters.extend([*"!@#$%^&*()"])
    if useNumbers:
        listOfCharacters.extend([*digits])
    if useLowerCase:
        listOfCharacters.extend([*ascii_lowercase])
    if useUpperCase:
        listOfCharacters.extend([*ascii_uppercase])
    return listOfCharacters
