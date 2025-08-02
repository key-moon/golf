def p(g):
	G,H=len(g),len(g[0]);D=[(A,B)for A in range(G)for B in range(H)if 0<g[A][B]!=8];I=min(A for(A,B)in D);J=min(A for(B,A)in D);L={(A-I,B-J):g[A][B]for(A,B)in D};K=[]
	for A in range(G):
		for B in range(H):
			if g[A][B]==8:
				C=[(A,B)];g[A][B]=0
				for M in range(len(C)):
					N,O=C[M]
					for(P,Q)in((1,0),(-1,0),(0,1),(0,-1)):
						E,F=N+P,O+Q
						if 0<=E<G and 0<=F<H and g[E][F]==8:g[E][F]=0;C.append((E,F))
				K.append((min(A for(A,B)in C),min(A for(B,A)in C)))
	for(A,B)in D:g[A][B]=0
	for(I,J)in K:
		for((R,S),T)in L.items():g[I+R][J+S]=T
	return g