def	p(j):
	B=[l[:]for	l	in	j];c,C=len(j),len(j[0]);k,A,l=c-1,0,1
	while	k>=0:
		B[k][A]=1
		if	0<=A+l<C:k-=1;A+=l
		else:k-=1;l=-l;A+=l
	return	B