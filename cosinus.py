import math


def factorial(x):
	t=1
	for k in range(1,x+1):
		t*=k
	return t
def cos(x):
	a=0
	for k in range(10):
		a+= ((-1)**k)*((x**(2*k))/(factorial(2*k)))
	return a
