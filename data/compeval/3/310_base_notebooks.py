from	collections	import	Counter
def	p(m):
	c=Counter(e	for	r	in	m	for	e	in	r	if	e).most_common()
	if	not	c:return[]
	l=c[-1][0];A=p=-1
	for(i,r)in	enumerate(m):
		if	l	in	r:
			if	A<0:A=i
			p=i
	B=C=-1
	for	i	in	range(len(m[0])):
		if	any(m[j][i]==l	for	j	in	range(A,p+1)):
			if	B<0:B=i
			C=i
	return[r[B:C+1]for	r	in	m[A:p+1]]