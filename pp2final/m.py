chars = []
s = input()
for i in s:
    chars.append(i)
counters = {}

for i in sorted(chars):
	if i in counters:
		counters[i] += 1
	else:
		counters[i] = 1

print(len(counters.values()))
for i, count in counters.items():
	print(i, count)