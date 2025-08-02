def p(g):
	F,G=len(g),len;H=G(g[0]);C=D=A=0;I=[(0,1),(1,0),(0,-1),(-1,0)]
	while 1:
		B=(H if A%2<1 else F-1)-2*(A//2)
		if B<1:break
		J,K=I[A%4]
		for E in range(B):g[C][D]=3;C+=J*(E<B-1);D+=K*(E<B-1)
		A+=1
	return g