def	p(j):
	from	collections	import	Counter	as	A;B=[v	for	k	in	j	for	v	in	k	if	v];c=dict(A(B).most_common());C=len(j[0]);k=[[0]*C	for	_	in	range(len(j))]
	for(D,l)in	enumerate(sorted(c,key=c.get,reverse=True)):k[-1-D][-c[l]:]=[l]*c[l]
	return	k