def permutations(array):
    if len(array) <= 1:
        return [array]
    result = []

    for i in range(len(array)):
        elem = array[i]
        rest = array[:i] +  array[i+1:]
        for j in permutations(rest):            
            result.append([elem] + j)
    return result

pre = permutations([3,4,5])
print(pre)