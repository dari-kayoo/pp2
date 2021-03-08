numbers = list(map(int, input().split()))
multipleOfNums = 1
for i in range(len(numbers)):
    multipleOfNums *= numbers[i]
print(multipleOfNums)    