def p(A):
	for(B,D)in enumerate(A):
		if 8 in D:C=D.index(8);break
	E=[A[C-1:C+2]for A in A[B-1:B+2]];F=[A[B-1][C],A[B+1][C],A[B][C-1],A[B][C+1]];E[1][1]=max(F,key=F.count);return E