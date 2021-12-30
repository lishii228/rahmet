import math
import matplotlib.pyplot as plt

import numpy as np

def factorial(x):
	t=1
	for k in range(1,x+1):
		t*=k
	return t
def sin(x):
	a=0
	for k in range(10):
		a+= ((-1)**k)*((x**(2*k+1))/(factorial(2*k+1)))
	return a

