def fibo(n):
	pool = [1, 1]
	if n == 1 or n == 2:
		return pool[n-1]
	else:
		for i in range(2, n):
			pool.append(pool[i-1] + pool[i-2])
	return pool[-1]

print(fibo(6))