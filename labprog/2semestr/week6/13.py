def pascalTriangle(n):
    throw = [1]
    y = [0]
    for i in range(max(n, 0)):
        print(throw)
        throw = [l+r for l,r in zip(throw+y, y+throw)]
    return n>=1    
pascalTriangle(int(input()))    
