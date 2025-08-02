def p(g):
	A,B=len(g),len(g[0]);F=[(A,C,g[A][C])for A in range(A)for C in range(B)if g[A][C]];G=[[0]*B for A in range(A)]
	for C in range(A):
		for D in range(B):
			E=[abs(C-A)+abs(D-B)for(A,B,E)in F];H=min(E)
			if E.count(H)==1:
				I,J,K=F[E.index(H)]
				if max(abs(C-I),abs(D-J))%2<1:G[C][D]=K
	return G