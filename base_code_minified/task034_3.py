def p(g):
	A,Q=len(g),len(g[0]);B=Q;F=[[0]*B for A in range(A)]
	for G in range(A-1):
		for H in range(B-1):
			C=[g[G+A][H+B]for A in(0,1)for B in(0,1)]
			if C.count(2)==1 and(R:=set(C)-{2}):
				S=R.pop();T=C.index(2);I,J=divmod(T,2);K=-1 if I<1 else 1;L=-1 if J<1 else 1;M=[-L,K];D,E=G+I,H+J
				while 0<=D<A and 0<=E<B:
					for N in(-1,0,1):
						O,P=D+M[0]*N,E+M[1]*N
						if 0<=O<A and 0<=P<B:F[O][P]=S
					D+=K;E+=L
				return F