a = list(map(str, input().split()))
a_set = set(a)
most = None
count_most = 0

for i in a_set:
    k = a.count(i)
    if k > count_most:
        count_most = k
        most = i

print(most.upper())