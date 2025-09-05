def	f(j,p,A,c,E,k):
	for	B	in	range(A,E+1):
		for	l	in	range(p,c+1):j[B][l]=k
def	z(j,p,A,c,E):f(j,p,A,c,E,4);f(j,p+1,A+1,c-1,E-1,2);j[A][p]=j[A][c]=j[E][p]=j[E][c]=1
def	p(j):
	C,a=len(j),len(j[0])
	for	D	in	range(C*a):
		l,B=D%a,D//a
		if	j[B][l]==5:
			c,A=l,B
			while	c<a-1and	j[A][c+1]==5:c+=1
			while	A<C-1and	j[A+1][c]==5:A+=1
			z(j,l,B,c,A)
	return	j