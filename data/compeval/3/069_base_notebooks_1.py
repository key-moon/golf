def	p(j,A=enumerate):
	c=[]
	for(B,k)in	A(j):
		for(C,l)in	A(k):
			if	l	not	in[0,8]:c+=[[B,C,l]];j[B][C]=0
	D=c[0][:];c=[[c[0]-D[0],c[1]-D[1],c[2]]for	c	in	c]
	for(B,k)in	A(j):
		for(C,l)in	A(k):
			if	l==8:
				j[B][C]=D[2]
				for	a	in	c:j[B+a[0]][C+a[1]]=a[2]
	return	j