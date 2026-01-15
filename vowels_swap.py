# swap vowels in a string
def swapVowels(inp: str) -> str:
    l = 0
    r = len(inp) - 1
    char = list(inp)
    while l < r:
        while inp[l] not in vowels:
            l += 1
        while inp[r] not in vowels:
            r -= 1
        char[l], char[r] = char[r], char[l]
        l += 1
        r -= 1        
    return ''.join(char)

word = "hello" 
vowels = {"a","e","i","o","u"}
print(swapVowels(word)) 
