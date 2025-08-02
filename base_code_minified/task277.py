def p(g):
	D=len(g);G=[]
	for H in range(D):
		for I in range(D):
			if g[H][I]==8:
				A=[(H,I)];g[H][I]=0
				for(B,C)in A:
					for(E,F)in((B+1,C),(B-1,C),(B,C+1),(B,C-1)):
						if 0<=E<D and 0<=F<D and g[E][F]==8:g[E][F]=0;A.append((E,F))
				G.append(A)
	J=min(map(len,G))
	for A in G:
		for(B,C)in A:g[B][C]=1+(len(A)==J)
	return g