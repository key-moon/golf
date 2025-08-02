def p(A):
	B={}
	for(D,L)in enumerate(A):
		for(E,F)in enumerate(L):
			if F:B.setdefault(F,[]).append((D,E))
	G=sorted(B,key=lambda H:len(B[H]));H,M=G[0],G[-1];C,N=B[M],B[H];I,O=min(A[0]for A in C),max(A[0]for A in C);J,P=min(A[1]for A in C),max(A[1]for A in C);Q=(O-I+1)//3;R=(P-J+1)//3;K=[[0]*3 for A in[None]*3]
	for(D,E)in N:K[(D-I)//Q][(E-J)//R]=H
	return K