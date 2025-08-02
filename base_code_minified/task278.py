def p(g):
	K,L=len(g),len(g[0]);I={(A,B)for A in range(K)for B in range(L)if g[A][B]==2}
	while I:
		M,N=I.pop();E=F=M;G=H=N;J=[(M,N)]
		while J:
			A,B=J.pop()
			for(C,D)in((A+1,B),(A-1,B),(A,B+1),(A,B-1)):
				if(C,D)in I:
					I.remove((C,D));J.append((C,D))
					if C<E:E=C
					elif C>F:F=C
					if D<G:G=D
					elif D>H:H=D
		if F>E or H>G:
			for A in range(E-1,F+2):
				if 0<=A<K:
					for B in range(G-1,H+2):
						if 0<=B<L and g[A][B]==0 and(A<E or A>F or B<G or B>H):g[A][B]=3
	return g