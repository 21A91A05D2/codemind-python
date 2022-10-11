def canConstruct(ransomNote,magazine):
    check= set(ransomNote)
    for i in check:
        if ransomNote.count(i)> magazine.count(i):
            return False
    return True


s=input()
s=s.split(" ")
ransomNote=s[0]
magazine=s[1]
print(canConstruct(ransomNote,magazine))
    

