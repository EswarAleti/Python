def sum_harmonic_series(n):
	return sum(1/q for q in range(1,n))
def sum_square_roots(n):
	return sum(q**0.5 for q in range(1,n))
print(sum_harmonic_series(4))
print(sum_square_roots(4))