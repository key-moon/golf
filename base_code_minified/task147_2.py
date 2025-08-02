def p(g):
	I=0;J=[];D=set();K,L=len(g),len(g[0])
	for E in range(K):
		for F in range(L):
			if g[E][F]==3 and(E,F)not in D:
				A=[(E,F)];D.add((E,F))
				for(G,H)in A:
					for(M,N)in((1,0),(-1,0),(0,1),(0,-1)):
						B,C=G+M,H+N
						if 0<=B<K and 0<=C<L and g[B][C]==3 and(B,C)not in D:D.add((B,C));A.append((B,C))
				if len(A)>I:I=len(A);J=A
	for(G,H)in J:g[G][H]=8
	return g