j=lambda	A,c,E:[[c	if	i==E	else	E	for	i	in	r]for	r	in	A]
def	p(A):
	k,E=len(A),len(A[0]);l,B,c,C=k,0,E,0
	for	a	in	range(k):
		for	D	in	range(E):
			if	A[a][D]:l,B,c,C=min(l,a),max(B,a),min(c,D),max(C,D)
	return	j([r[c:C+1]for	r	in	A[l:B+1]],A[l][c],A[l+(B-l)//2][c+(C-c)//2])