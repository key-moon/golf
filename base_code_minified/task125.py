def p(g):
	M=len(g);N=len(g[0]);K=set()
	for C in range(M):
		for D in range(N):
			if g[C][D]==6 and(C,D)not in K:
				L=[(C,D)];K.add((C,D));E=F=C;G=H=D
				while L:
					I,J=L.pop()
					if I<E:E=I
					if J<G:G=J
					if I>F:F=I
					if J>H:H=J
					for(O,P)in((1,0),(-1,0),(0,1),(0,-1)):
						A,B=I+O,J+P
						if 0<=A<M and 0<=B<N and g[A][B]==6 and(A,B)not in K:K.add((A,B));L+=[(A,B)]
				E-=1;G-=1;F+=1;H+=1
				for A in range(E,F+1):
					for B in range(G,H+1):
						if A in(E,F)or B in(G,H):g[A][B]=3
						elif g[A][B]!=6:g[A][B]=4
	return g