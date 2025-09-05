j=len
A=range
def	p(c):
	D,k=j(c),j(c[0]);B=[a	for	A	in	c	for	a	in	A];B=sorted(B)[-1];c=[[0]+A+[0]for	A	in	c];l=[[0]*(k+2)];c=l+c+l;E=[[1,1],[-1,-1],[-1,1],[1,-1],[0,1],[0,-1],[-1,0],[1,0],[0,0]]
	for	a	in	A(1,D+1):
		for	C	in	A(1,k+1):
			if	c[a][C]==B:
				e=[c[A[0]+a][A[1]+C]for	A	in	E]
				if	sum(e)==B:c[a][C]=0
	c=c[1:-1];c=[A[1:-1]for	A	in	c];return	c