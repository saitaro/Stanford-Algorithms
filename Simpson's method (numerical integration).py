from math import *

def simpson(func, x, i):
	term = x/(3*i)
	# print('term:', term)
	summa = 0
	for j in range(i+1):
		if j == 0:
			summa += func(0)
			# print('first', func(0))
		elif j == i:
			summa += func(x)
			# print('last', func(x))
		else:
			if j % 2:
				summa += 4*func((j*x)/i)
				# print('4', 4*func((j*x)/i))
			else:
				summa += 2*func((j*x)/i)
				# print('2', 2*func((j*x)/i))
	return term*summa

print(simpson(lambda x: e**(-x**2), 3, 8))