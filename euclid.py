def gcd(a,b):
	if a==b:
		return a
	if a<b:
		return gcd(b,a)
	if a==1 or b==1:
		return 1
	if a==0:
		return b
	if b==0:
		return a
	if a>b:
		return gcd(a-b,b)