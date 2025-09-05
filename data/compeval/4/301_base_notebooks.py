def	p(j):
	from	collections	import	Counter	as	A;B=[c	for	l	in	j	for	c	in	l	if	c];c=dict(A(B).most_common());C=len(j[0]);k=[[0]*C	for	c	in	range(len(j))]
	for(D,l)in	enumerate(sorted(c,key=c.get,reverse=True)):k[-1-D][-c[l]:]=[l]*c[l]
	return	k