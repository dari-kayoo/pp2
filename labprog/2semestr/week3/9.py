a, b = [int(i) for i in (input().split())]
A,B = set(), set()   
for i in range(a):
    A.add(int(input()))
for i in range(b):
    B.add(int(input()))
print(len(set(A)&set(B)))      
print(*sorted(set(A)&set(B)))
print(len(set(A)-set(B)))  
print(*sorted(set(A)-set(B)))
print(len(set(B)-set(A)))  
print(*sorted(set(B)-set(A)))
