def	p(g):
	B=range;G=[A[:]for	A	in	g];H,I=len(g),len(g[0]);K=[(A,C)for	A	in	B(H)for	C	in	B(I)if	g[A][C]==8]
	for(C,D)in	K:
		for(E,F)in[(0,1),(1,0),(0,-1),(-1,0)]:
			A=1
			while	0<=C+A*E<H	and	0<=D+A*F<I:
				if	g[C+A*E][D+A*F]==8:
					for	J	in	B(1,A):G[C+J*E][D+J*F]=3
					break
				A+=1
	return	G