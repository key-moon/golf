def p(g):
	J,C=len(g),len(g[0]);M=[[0]*C for A in g];D=[[0]*C for A in g]
	for E in range(J):
		for F in range(C):
			if g[E][F]and not D[E][F]:
				G=[(E,F)];D[E][F]=1
				for R in G:
					H,I=R
					for(K,L)in((1,0),(-1,0),(0,1),(0,-1)):
						A,B=H+K,I+L
						if 0<=A<J and 0<=B<C and g[A][B]and not D[A][B]:D[A][B]=1;G.append((A,B))
				N,O=zip(*G);P,Q=(min(N)+max(N))//2,(min(O)+max(O))//2
				for(H,I)in G:K,L=H-P,I-Q;M[J-1-P-L][Q+K]=g[H][I]
	return M