def p(g):
	C,D=len(g),len(g[0]);F=max({B for A in g for B in A},key=lambda x:sum(A.count(x)for A in g));I=[(A,B,g[A][B])for A in range(C)for B in range(D)if g[A][B]!=F and sum(0<=A+E<C and 0<=B+F<D and g[A+E][B+F]==g[A][B]for(E,F)in((1,0),(-1,0),(0,1),(0,-1)))<2]
	for A in range(C):
		for B in range(D):
			if g[A][B]==F:
				G=10**9;E=None
				for(J,K,L)in I:
					H=abs(A-J)
					if H==abs(B-K)<G:G=H;E=L
				if E is not None:g[A][B]=E
	return g