def	p(g):
	h,w=len(g),len(g[0]);b=[(i,j)for	i	in	range(h)for	j	in	range(w)if	g[i][j]==2];a=[(i,j)for	i	in	range(h)for	j	in	range(w)if	g[i][j]==3];k=0if	all(i==b[0][0]for(i,j)in	b)else	1;C=min(x[k]for	x	in	b);E=max(x[k]for	x	in	b);D=min(x[k]for	x	in	a);A=max(x[k]for	x	in	a)
	if	A<C:d=C-1-A;B=D+d-1
	else:d=E+1-D;B=A+d+1
	r=[[0]*w	for	_	in	range(h)]
	for(i,j)in	b:r[i][j]=2
	for(i,j)in	a:r[i+(1-k)*d][j+k*d]=3
	for	u	in	range(h	if	k	else	w):r[u	if	k	else	B][B	if	k	else	u]=8
	return	r