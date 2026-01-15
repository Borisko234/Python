# find middle number in an array
def middleFinder(arr):
    slow = fast = 0
    while fast + 2 <= len(arr):
        slow += 1
        fast += 2
    return arr[slow]

array = [1,2,3,4,5]
print(middleFinder(array))