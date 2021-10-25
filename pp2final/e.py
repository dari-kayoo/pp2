import math
def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

raw_numbers = []
while True:
    try:
        raw_numbers += input().split()
    except EOFError:
        break

numbers = []
for number in raw_numbers:
    numbers.append(int(number))

counters = {}
f = []
for i in numbers:
    if not is_prime(i):
        if i not in counters:
            counters[i] = 1
        else:
            counters[i] += 1

        if counters[i] == 2:
            f.append(i)

for i in sorted(f):
    print(i, end=' ')
