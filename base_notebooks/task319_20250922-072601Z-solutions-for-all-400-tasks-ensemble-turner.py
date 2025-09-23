def p(g):
	if not g or not g[0]:return[list(A)for A in g]
	E=tuple(tuple(A)for A in g);U,V=len(E),len(E[0]);F=lambda x:(min(A for(A,B)in x),min(A for(B,A)in x),max(A for(A,B)in x),max(A for(B,A)in x))if x else(0,0,0,0);J=lambda x:{(A-F(x)[0],B-F(x)[1])for(A,B)in x}if x else set();G=tuple(tuple(A[::-1])for A in E);from collections import Counter as W;K=max(W(sum(G,())).items(),key=lambda kv:kv[1])[0];A={};[A.setdefault(G[B][C],set()).add((B,C))for B in range(U)for C in range(V)if G[B][C]!=K]
	if not A:return[list(A)for A in E]
	C=max(A,key=lambda c:len(A[c]));H=J(A[C]);B=None
	for(L,D)in A.items():
		if L==C or len(D)==len(A[C]):continue
		X=J(D);I={(2*A+C,2*B+D)for(A,B)in X for C in(0,1)for D in(0,1)}
		if I and H:M,N,O,P=[A for(A,B)in I],[A for(B,A)in I],[A for(A,B)in H],[A for(B,A)in H];Q=max(sum((C+A,D+B)in H for(C,D)in I)for A in range(min(O)-max(M),max(O)-min(M)+1)for B in range(min(P)-max(N),max(P)-min(N)+1))
		else:Q=0
		R=Q-2*len(D),len(D),F(D)[3],L;B=R if B is None or R>B else B
	S=B[3]if B else(lambda o:max(o,key=lambda c:len(A[c]))if o else C)([A for A in A if A!=C]);Y,Z,a,b=F(A[S]);T=[list(G[A][Z:b+1])for A in range(Y,a+1)];[[A.__setitem__(B,K)for B in range(len(A))if A[B]!=S]for A in T];return[list(A[::-1])for A in T]