def hhh(x):
c=[]
for k in range(len(x)):
	c.append(htable(x[k]))
return c


def htable(let):
	if let=='х':
		return 11
	if let== 'а':
		return 12
	if let== 'b':
		return 13
	if let== 'a':
		return 14
	else:
		return int(let)


def hash(pattern, Q):


	h=0
	for i in range(len(pattern)):
		h=(h*13+htable(pattern[i]))%Q
	return h

def robcarp(word,pattern):
	Q=127
	q=hash(pattern,Q)
	n=len(pattern)
	tb=[]
	m=hash(word[0:n],Q)
	word=hhh(word)

	if word==[]:
		return []


	for k in range(len(word)-n):
		if m==q :
			tb.append(k)
		m=((m-int(word[k])*(13**(n-1)))*13+int(word[k+n]))%Q
	return tb

i=robcarp('bababab','bab')
print(i)
