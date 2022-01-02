def inverse(a):
	z=[]
	for k in range(len(a)):
		z.append(a[-k-1]*a[-k-1])
	return z
p=inverse([0,1,32,-9])
print(p)