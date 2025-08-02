def p(g):
	B=len(g);J=[]
	for E in range(B):
		for F in range(B):
			if g[E][F]==5:
				A=[(E,F)];g[E][F]=0;G=0
				while G<len(A):
					H,I=A[G];G+=1
					for(K,L)in((1,0),(-1,0),(0,1),(0,-1)):
						C,D=H+K,I+L
						if 0<=C<B and 0<=D<B and g[C][D]==5:g[C][D]=0;A+=[(C,D)]
				J+=[A]
	for(M,A)in enumerate(sorted(J,key=len)):
		for(H,I)in A:g[H][I]=[2,4,1][M]
	return g