# move all special cahracters to the end of string
def moveSpecialChar(word:str) -> str:
    normalChar = []
    specialChar = []
    for char in word:
        if char.isalnum():
            normalChar.append(char)
        if not char.isalnum():
            specialChar.append(char)
    return ''.join(normalChar + specialChar)

word = "abs@de!fg"
print(moveSpecialChar(word))