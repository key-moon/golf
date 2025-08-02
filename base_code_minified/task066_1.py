def p(g):
	F,G=len(g),len(g[0]);H=[(A,B)for A in range(F)for B in range(G)if g[A][B]==3];M={(A,B)for A in range(F)for B in range(G)if g[A][B]==2};I=H[:];J=set(H);K={};E=1,0,-1,0,0,1,0,-1
	while I:
		A,B=I.pop(0)
		if any((A+E[C],B+E[C+1])in M for C in(0,2,4,6)):break
		for L in(0,2,4,6):
			C,D=A+E[L],B+E[L+1]
			if 0<=C<F and 0<=D<G and(C,D)not in J and g[C][D]==0:J.add((C,D));K[C,D]=A,B;I.append((C,D))
	while(A,B)not in H:g[A][B]=3;A,B=K[A,B]
	return g