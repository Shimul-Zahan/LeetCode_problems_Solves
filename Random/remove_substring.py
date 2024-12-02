def remove_pair(string):
    array = []
    i = 0
    while i < len(string):
        array.append(string[i])
        # if len(array) > 1 and ord(array[-2]) - ord(array[-1]) == -1:
        #     array.pop()
        #     array.pop()
        # i += 1
        if len(array) > 1 and ([array[-2], array[-1]] == ['A', 'B'] or [array[-2], array[-1]] == ['C', 'D']):
            array.pop()
            array.pop()
        i += 1
    ''.join(array)
    return len(array)

s = 'ACBBD'
print(remove_pair(s))