def p(A):
	D,E=len(A),len(A[0]);F=[(B,C)for B in range(D)for C in range(E)if A[B][C]];B=[A[B][C]for(B,C)in F];G=max({*B},key=B.count);H=next(A for A in{*B}if A!=G);I=[(2*A,2*B,C)for((A,B),C)in zip(F,B)];C=[(A,B)for(A,B,C)in I if C==H];J=sum(A for(A,B)in C)//len(C);K=sum(A for(B,A)in C)//len(C);P=max(abs(A-J)+abs(B-K)for(A,B,C)in I);L=[[0]*E for A in range(D)]
	for M in range(D):
		for N in range(E):
			O=abs(2*M-J)+abs(2*N-K)
			if O<=P:L[M][N]=G if O//2%2==0 else H
	return L