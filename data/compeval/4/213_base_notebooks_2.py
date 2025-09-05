def	Z(j,A):return	len(set([B[A]for	B	in	j]))
def	p(c):
	C=enumerate;k,D=len(c),len(c[0]);l=Z(c,0)+Z(c,-1)<len(set(c[0]))+len(set(c[-1]));c=[[A	if	A!=5else	0for	A	in	A]for	A	in	c]
	for(A,a)in	C(c):
		for(B,e)in	C(a):
			if	l:c[A][B]=max([c[0][B],c[-1][B]])
			else:c[A][B]=max([c[A][0],c[A][-1]])
	if	l:c=[[A	for	A	in	A	if	A>0]for	A	in	c];c=c[:len(c[0])]
	else:c=[A	for	A	in	c	if	sum(A)>0];c=[A[:len(c)]for	A	in	c]
	return	c