def isPangram(s):
    letterSet = set()
    for i in s:
        letterSet.add(i)
    if len(letterSet) == len(s):
        return True
    return False        
               
print(isPangram(input()))                    