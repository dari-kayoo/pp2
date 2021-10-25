def to_base(num, new_base):
	reversed_digits = []

	while num > new_base:
		reversed_digits.append(num % new_base)
		num //= new_base

	reversed_digits.append(num)

	converted = ''

	for i in reversed(reversed_digits):
		converted += str(i)

	return converted

a = int(input())
print(to_base(a, 7))