def p(A):
	B={}
	for P in A:
		for I in P:B[I]=B.get(I,0)+1
	J=sorted(B,key=lambda F:-B[F])[1];E=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==J];K=[A for(A,B)in E];L=[A for(B,A)in E];Q,R=min(K),max(K);S,T=min(L),max(L);F=[(B,C)for(B,C)in E if Q<B<R and S<C<T and A[B][C]!=J];from collections import Counter as U;C=U(A[B][C]for(B,C)in F);V=min(C,key=lambda T:C[T]);M=max(C,key=lambda T:C[T]);D=[(B,C)for(B,C)in F if A[B][C]==V][0]
	def W(A,B):return B,-A
	for(N,O)in F:
		if A[N][O]==M:
			G,H=N-D[0],O-D[1]
			for X in range(3):G,H=W(G,H);A[D[0]+G][D[1]+H]=M
	return A