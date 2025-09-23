def p(g,E=enumerate):
	H=len(g[0]);A=[-1]+[A for(A,B)in E(zip(*g))if not any(B)]+[H];B=[[C[A[B]+1:A[B+1]]for C in g]for B in range(len(A)-1)if A[B]+1<A[B+1]];C=B[:1]
	for D in B[1:]:I=C[-1];J=next((B for(B,A)in E(I)if A and A[-1]==5),0);K=next((B for(B,A)in E(D)if A and A[0]==5),0);F=J-K;G=[[0]*len(D[0])]*3;C+=[(G+D+G)[3-F:6-F]]
	L=[next((A for B in A for A in B if A>0 and A!=5),0)for A in B];M=[[[B if A==5 else A for A in A]for A in A]for(A,B)in zip(C,L)];return[sum(A,[])for A in zip(*M)]