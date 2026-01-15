# reverse order of words in a string
def string_reverse (inputStr):
    startString = endString = len(inputStr) - 1
    reversedString = ""  
    while startString >= 0:
        while inputStr[startString] != " " and startString >= 0:
            startString -= 1
        reversedString += inputStr[startString + 1:endString +1] + " "
        endString = startString - 1 
        startString -= 1
    return reversedString

stri = "a ab abc abcd abcdefgh"
print(string_reverse(stri))
