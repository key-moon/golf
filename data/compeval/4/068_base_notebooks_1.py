def	p(j):
	A={};c=range
	for	B	in	c(10):
		for	k	in	c(10):
			if	j[B][k]:A[j[B][k]]=A.get(j[B][k],0)+1
	D=next(A	for(A,c)in	A.items()if	c==1);l,A=next((A,B)for	A	in	c(10)for	B	in	c(10)if	j[A][B]==D);C=[[0]*10for	A	in	c(10)];C[l][A]=D
	for	a	in[-1,0,1]:
		for	E	in[-1,0,1]:
			if	a	or	E:
				e,F=l+a,A+E
				if	0<=e<10and	0<=F<10:C[e][F]=2
	return	C