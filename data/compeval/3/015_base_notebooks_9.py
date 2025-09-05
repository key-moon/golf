def	p(j,A=enumerate):
	c=[k[:]for	k	in	j]
	for(D,k)in	A(j):
		for(E,l)in	A(k):
			for	B	in-1,0,1:
				for	a	in-1,0,1:
					if	l	and	B|a	and(l==2and	B*a	or	l==1and	not	B*a):
						C=D+B;e=E+a
						if	0<=C<len(j)and	0<=e<len(j[0])and	c[C][e]<1:c[C][e]=4+3*(l&1)
	return	c