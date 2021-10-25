def count_letters(word):
    counts = {}
    for letter in word:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

    return counts


s = input()
l = []
while True:
    try:
        word = input()
    except EOFError:
        break

    l.append(word)

f = []

for word in l:
    if count_letters(word) != count_letters(s):
        f.append(word)

for word in sorted(f):
    print(word, end=' ')

print()
