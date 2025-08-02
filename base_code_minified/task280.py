def p(g):
	E,F=len(g),len(g[0])
	for G in range(E):
		for H in range(F):
			if g[G][H]==2:
				I=0
				for(A,B)in((-1,0),(1,0),(0,-1),(0,1)):
					C,D=G+A,H+B;J=0
					while 0<=C<E and 0<=D<F and g[C][D]==0:J+=1;C+=A;D+=B
					if J>I:I=J;N=A,B
				A,B=N
				for M in range(I+1):
					C,D=G+A*M,H+B*M;g[C][D]=2
					for(O,P)in((-B,A),(B,-A)):
						K,L=C+O,D+P
						if 0<=K<E and 0<=L<F and g[K][L]==0:g[K][L]=3
	return g