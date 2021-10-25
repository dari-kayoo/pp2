words = []
while True:
    try:
        words += input().split()
    except EOFError:
        break

counters = {}

for i in sorted(words):
	if i in counters:
		counters[i] += 1
	else:
		counters[i] = 1

for i, count in counters.items():
	print(i, count)