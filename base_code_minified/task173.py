def p(g):
	J,K=len(g),len(g[0]);M={}
	for(H,I)in((0,1),(1,1)):
		for A in range(J):
			for B in range(K):
				C,D=A-H,B-I;E,F=A+H,B+I
				if 0<=C<J and 0<=D<K and 0<=E<J and 0<=F<K:
					G=g[C][D];L=g[A][B];O=g[E][F]
					if G and G==O and L and L!=G:M[H,I]=G,L;break
			if(H,I)in M:break
	if(0,1)in M:
		G,L=M[0,1];N=[(0,1),(0,-1),(1,0),(-1,0)]
		for A in range(J):
			for B in range(K):
				for(H,I)in N:
					C,D=A-H,B-I;E,F=A+H,B+I
					if 0<=C<J and 0<=D<K and 0<=E<J and 0<=F<K:
						if g[A][B]==L and not g[C][D]and not g[E][F]:g[C][D]=g[E][F]=G
						if not g[A][B]and g[C][D]==G and g[E][F]==G:g[A][B]=L
	if(1,1)in M:
		G,L=M[1,1];N=[(1,1),(1,-1),(-1,1),(-1,-1)]
		for A in range(J):
			for B in range(K):
				for(H,I)in N:
					C,D=A-H,B-I;E,F=A+H,B+I
					if 0<=C<J and 0<=D<K and 0<=E<J and 0<=F<K:
						if g[A][B]==L and not g[C][D]and not g[E][F]:g[C][D]=g[E][F]=G
						if not g[A][B]and g[C][D]==G and g[E][F]==G:g[A][B]=L
	return g