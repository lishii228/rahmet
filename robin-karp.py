def hash(pattern, Q):
	h=0
	for i in range(len(pattern)):
		h=(h*13+int(pattern[i]))%Q
	return h

def robcarp(word,pattern):
	Q=127
	q=hash(pattern,Q)
	n=len(pattern)
	tb=[]
	m=hash(word[0:n],Q)


	for k in range(len(word)-n):
		if hash(word[k:k+n],Q)==q :
			tb.append(k)
		m=((m-int(word[k])*(13**(n-1)))*13+int(word[k+n]))%Q
	return tb

i=robcarp('1259130123509743185942493578955781254671381765745','2')
print(i)