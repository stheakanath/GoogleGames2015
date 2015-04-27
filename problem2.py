n = 2
while (n < 10**100):
	n *= 2
sumDig = lambda n : n if (n < 10) else (n%10 + sumDig(n//10))
print(sumDig(n))