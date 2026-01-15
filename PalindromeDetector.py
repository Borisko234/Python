# decide whether input is polindrome or not
def palindrome_detector(inpStr):
    left = 0
    right = len(inpStr) - 1
    while left < right:
        while not inpStr[left].isalnum():
          left += 1
        while not inpStr[right].isalnum():
          right -= 1
        if inpStr[left].lower() != inpStr[right].lower():
            return False
        left += 1
        right -= 1
    
    return True
