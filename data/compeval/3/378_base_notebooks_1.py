def	f(j,A,c,E,k):
	B=j[A][c]
	if	B==0:return
	if	not	sum(j[A][c+i]==B	for	i	in(1,-1))==sum(j[A+i][c]==B	for	i	in(1,-1))==1:return
	l,C,p,a=2*(j[A+1][c]==B)-1,2*(j[A][c+1]==B)-1,c,A
	if	j[A+l][c+C]==B:return
	while	1<=p<k-1and	1<=a<E-1:a-=l;p-=C;j[a][p]=j[A+2*l][c+2*C]
def	p(j):
	A,k=len(j),len(j[0])
	for	B	in	range(1,A-1):
		for	c	in	range(1,k-1):f(j,B,c,A,k)
	return	j