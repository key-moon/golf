def	p(j,A=enumerate):
	c=[[0]*len(j[0])for	_	in	j]
	for	B	in	set(sum(j,[]))-{0}:
		k=[(C,a)for(C,r)in	A(j)for(a,x)in	A(r)if	x==B];D,l=max(A	for(A,_)in	k),max(a	for(_,a)in	k)
		for(C,a)in	k:c[C][a+(C<D	and	a<l)]=B
	return	c