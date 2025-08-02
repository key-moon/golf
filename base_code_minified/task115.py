def p(A):
	D=len({*A[0]})>1;F=A[0]if D else[A[0]for A in A];B=[];E=None
	for C in F:
		if C!=E:B+=[C];E=C
	return D and[B]or[[A]for A in B]