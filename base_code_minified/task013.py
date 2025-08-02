def p(g):
	I=[(B,D,A)for(B,C)in enumerate(g)for(D,A)in enumerate(C)if A];(D,E,F),(G,J,H)=I
	if D*G:
		A=G-D
		for(K,B)in enumerate(g):
			for C in range(len(B)):B[C]=F if(K-D)%(A*2)<A else H
	else:
		A=J-E
		for B in g:
			for C in range(len(B)):B[C]=F if(C-E)%(A*2)<A else H
	return g