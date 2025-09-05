def	p(j,A=enumerate):
	c=[[l	for(A,l)in	A(k)]for	k	in	j]
	for(C,k)in	A(j):
		for(D,l)in	A(k):
			if	l==2:
				for	B	in	range(-1,2):
					for	a	in	range(-1,2):
						try:
							if[B,a]!=[0,0]and	C+B>-1and	D+a>-1:c[C+B][D+a]=1
						except:0
	return	c