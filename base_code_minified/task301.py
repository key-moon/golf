def p(A):
	I,C=len(A),len(A[0]);F=[]
	for G in A:
		B=0
		while B<C:
			D=G[B]
			if D:
				E=B+1
				while E<C and G[E]==D:E+=1
				F+=[(E-B,D)];B=E
			else:B+=1
	F.sort(reverse=1);H=[[0]*C for A in A]
	for(J,(K,D))in enumerate(F):
		for B in range(C-K,C):H[I-1-J][B]=D
	return H