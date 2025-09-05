def	p(g):
	h,w=len(g),len(g[0]);A=[g[i][j]for	i	in	range(h)for	j	in	range(w)];A=A[::-1];B=[[0]*w	for	_	in	range(h)]
	for(C,D)in	enumerate(A):i,j=C//w,C%w;B[i][j]=D
	return	B