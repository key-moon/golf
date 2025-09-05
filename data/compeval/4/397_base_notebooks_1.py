def	p(j,A=range):
	c,D=len(j),len(j[0]);k=[]
	for	B	in	A(c-1):
		for	l	in	A(D-1):
			C=j[B][l],j[B][l+1],j[B+1][l],j[B+1][l+1]
			if	all(C):k+=[(B,l,len(set(C)))]
	for(B,l,a)in	k:
		for	E	in	A(a):
			e=B+2+E
			if	e<c:j[e][l]=j[e][l+1]=3
	return	j