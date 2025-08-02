def p(g):
	A=len(g);C=[(A,B)for A in range(A)for B in range(len(g[0]))if g[A][B]==3];D=min(A for(A,B)in C)+.5;E=min(A for(B,A)in C)+.5
	for F in range(A):
		for G in range(len(g[0])):
			B=g[F][G]
			if B and B!=3:
				J=F-D;K=G-E
				for(L,M)in((1,1),(1,-1),(-1,1),(-1,-1)):
					H=int(D+L*J);I=int(E+M*K)
					if 0<=H<A and 0<=I<len(g[0]):g[H][I]=B
	return g