def	p(j):
	C=range;c=len(j);D=[[0]*c	for	A	in	C(c)];k,A=0,0;l=[(0,1),(1,0),(0,-1),(-1,0)]
	for	E	in	C(c):
		D[k][A]=3
		if	E<c-1:A+=1
	a=c-1;B=1
	while	a>0:
		for	e	in	C(2):
			if	a>0:
				k,A=k+l[B][0],A+l[B][1]
				for	E	in	C(a):
					D[k][A]=3
					if	E<a-1:k,A=k+l[B][0],A+l[B][1]
				B=(B+1)%4
		a-=2
	return	D