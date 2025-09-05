L=len
R=range
def	p(g):
	h,w=L(g),L(g[0]);A=[x	for	r	in	g	for	x	in	r];A=sorted(A)[-1];g=[[0]+A+[0]for	A	in	g];B=[[0]*(w+2)];g=B+g+B;C=[[1,1],[-1,-1],[-1,1],[1,-1],[0,1],[0,-1],[-1,0],[1,0],[0,0]]
	for	r	in	R(1,h+1):
		for	c	in	R(1,w+1):
			if	g[r][c]==A:
				D=[g[i[0]+r][i[1]+c]for	i	in	C]
				if	sum(D)==A:g[r][c]=0
	g=g[1:-1];g=[A[1:-1]for	A	in	g];return	g