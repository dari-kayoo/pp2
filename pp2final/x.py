n = int(input())
scores = {}
total = 0
for i in range(n):
	raw_score = input().split()

	name = raw_score[0]
	score = int(raw_score[1])

	if name in scores:
		scores[name] += score
	else:
		scores[name] = score

	total += score


pairs = sorted(scores.items(), key=lambda x: x[1], reverse=True)

for pair in pairs:
	print(f'{pair[0]} {pair[1] * 100 / total:.5f}%')