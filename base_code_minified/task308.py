def p(A):
	C=max({B for A in A for B in A},key=lambda D:sum(A.count(D)for A in A));E,F=len(A),len(A[0]);H,I=E//2,F//2;D=[(B-H,D-I,A[B][D])for B in range(E)for D in range(F)if A[B][D]!=C]
	if not D:return[[C]]
	B=max(max(abs(A),abs(B))for(A,B,C)in D);G=[[C]*(2*B+1)for A in range(2*B+1)]
	for(J,K,L)in D:G[J+B][K+B]=L
	return G