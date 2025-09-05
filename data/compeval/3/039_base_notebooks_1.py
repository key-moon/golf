L=len
R=range
def	p(g):
	h,w=L(g),L(g[0]);A=[]
	for	r	in	R(h):
		for	c	in	R(w):
			if	g[r][c]>0:A.append([r,c])
	D=min([i[1]for	i	in	A]);B=max([i[1]for	i	in	A]);E=min([i[0]for	i	in	A]);C=max([i[0]for	i	in	A]);B=B-(B-D)//2;C=C-(C-E)//2;g=g[E:C];g=[A[D:B]for	A	in	g];return	g