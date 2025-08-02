def p(g):
	H=[(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==8];(C,D),(E,F)=H;I,J=(E-C)//abs(E-C),(F-D)//abs(F-D)
	for(K,L)in((C,D),(E,F)):
		for G in(1,-1):
			A,B=K,L
			while 1:
				A+=G*I;B+=G*J
				if g[A][B]==2:break
				if g[A][B]==0:g[A][B]=3
	return g