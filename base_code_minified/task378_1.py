def p(g):
	E,F=len(g),len(g[0]);D={}
	for G in range(E):
		for H in range(F):
			I=g[G][H]
			if I:D.setdefault(I,[]).append((G,H))
	O=max(D,key=lambda k:len(D[k]));J=min(D,key=lambda k:len(D[k]));K,L=D[J][0]
	for(M,N)in((1,1),(1,-1),(-1,1),(-1,-1)):
		A=1
		while True:
			B,C=K+M*A,L+N*A
			if B<0 or C<0 or B>=E or C>=F:break
			if g[B][C]==O:
				A+=1
				while True:
					B,C=K+M*A,L+N*A
					if B<0 or C<0 or B>=E or C>=F:break
					g[B][C]=J;A+=1
				break
			A+=1
	return g