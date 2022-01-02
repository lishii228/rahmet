def prime(p):
	if p==2:
		return True
	if p==4:
		return False
	a=list(range(2,p+1))
	b=[2]
	for i in range(p+1):
		for k in a:
			if k%b[-1]==0:
				a.remove(k)
			if a!=[]:
				b.append(a[0])
	if b[-1]==p:
		return True
	else:
		return False


for k in range(1,1000):
	print([k,prime(k)])
