def p(A):
	B=next(B for B in range(len(A))if len(set(A[B]))==1);C=next(B for B in range(len(A[0]))if len({A[B]for A in A})==1)
	for E in(range(B),range(B+1,len(A))):
		for F in(range(C),range(C+1,len(A[0]))):
			D=[[A[B][C]for C in F]for B in E]
			if len(set(sum(D,[])))>1:return D