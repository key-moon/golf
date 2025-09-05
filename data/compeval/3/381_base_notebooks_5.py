def	p(j,A=range):
	c=len(j)
	for	D	in	A(1,c-1):
		k=B=0
		for	l	in	A(c):
			C=j[D][l];k=[k,1][k<1and	C>1]
			if	k==1and	C<1:k=2;B=[B,l][~B]
			if	k>1and	C>1:
				for	a	in	A(B,l):j[D][a]=9;k=1;B=0
	return	j