class matrix(object):
	"""docstring for matrix"""
	def __init__(self, a1,a2,a3,a4):
		self.a1 = a1
		self.a2 = a2
		self.a3=a3
		self.a4=a4

	def tr(self):
		return self.a1+self.a4
	def det(x):
		return self.a1*self.a4-self.a2*self.a3
	def __add__(x,y):
		a1=x.a1+y.a1
		a2=x.a2+y.a2
		a3=x.a3+y.a3
		a4=x.a4+y.a4
		return matrix(a1,a2,a3,a4)
	def __sub__(x,y):
		a1=x.a1-y.a1
		a2=x.a2-y.a2
		a3=x.a3-y.a3
		a4=x.a4-y.a4
	def __mul__(x,y):
		a1=x.a1*y.a1+x.a2*y.a3
		a2=x.a3*y.a1+x.a4*y.a3
		a3=x.a1*y.a2+x.a2*y.a4
		a4=x.a3*y.a2+x.a4*y.a4
	def show(self):	
		print([self.a1,self.a2])
		print([self.a3,self.a4])



	def __pow__(a,n):
		if n==0:
			return matrix(1,0,0,1)
		if n==1:
			return a
		if n>1:
			return a*__pow__(a,n-1)
		if n == -1:
			return matrix[a.a4/a.det(),-a.a2/a.det(),-a.a3/a.det(),a.a1/a.det()]
		if n<-1:
			return __pow__(a,-1)* __pow__(a,n+1)
	def __truediv__(a,b):
		return a*__pow__(b,-1)
		pass
z=matrix(1,2,3,4)
z.show()
c=matrix(4,2,6,-1)
v=z+c
v.show()
