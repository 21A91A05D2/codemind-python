def countWords(st):
    count = 1
    for i in range(1, len(st) - 1):
        if (st[i].isupper()):
            count += 1
 
    return count
 
# Driver code
st = input()
print(countWords(st))