import math

def primeDivisors(_n):
	primeDiv = []
	if _n <=3:
		return [_n]
	else:
		d = 2
		n = _n
		while d <= int(math.sqrt(_n)+1):
			if _n % d != 0:
				d += 1
			else:
				while _n % d == 0:
					_n //= d
				primeDiv.append(d)

		if _n != 1:
			primeDiv.append(_n)
		if _n == n:
			primeDiv = [_n]

		return primeDiv

print(primeDivisors(2))
print(primeDivisors(7))
print(primeDivisors(16))
print(primeDivisors(99))
