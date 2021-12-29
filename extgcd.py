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
		return gcd(a%b,b)


def extgcd(a,b):
	if a==1:
		return [1,0]
	if b==1:
		return [0,1]
	if gcd(a,b)!=1 :
		return [extgcd(a//gcd(a,b),b//gcd(a,b))[0] ,extgcd(a//gcd(a,b),b//gcd(a,b))[1]]
	if b>a:
		return [extgcd(b,a)[1] ,extgcd(b,a)[0]]
	return [extgcd(a%b ,b)[0],extgcd(a%b,b)[1]-(a//b)*extgcd(a%b,b)[0]]

print(extgcd(22,121))

	#ax + by = 1
	#a = kb +m 
	#mx+ b(y+kx)=1

		