def p(g):
	N,K=len(g),len(g[0]);E=[[0]*K for A in g];L=[]
	for F in range(N):
		for G in range(K):
			if g[F][G]and not E[F][G]:
				H=[(F,G)];E[F][G]=1
				for(A,B)in H:
					for(S,T)in((1,0),(-1,0),(0,1),(0,-1)):
						C,D=A+S,B+T
						if 0<=C<N and 0<=D<K and g[C][D]and not E[C][D]:E[C][D]=1;H.append((C,D))
				L.append((H,[g[A][B]for(A,B)in H]))
	if len(L)!=2:return g
	(I,U),(J,V)=L;O=min(A for(A,B)in I);P=min(A for(B,A)in I);Q=min(A for(A,B)in J);R=min(A for(B,A)in J)
	for(A,B)in I:g[A][B]=0
	for(A,B)in J:g[A][B]=0
	for((A,B),M)in zip(I,U):g[Q+(A-O)][R+(B-P)]=M
	for((A,B),M)in zip(J,V):g[O+(A-Q)][P+(B-R)]=M
	return g