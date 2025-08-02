def p(g):
	I,J=len(g),len(g[0]);G=[]
	for B in range(I):
		for C in range(J):
			if g[B][C]==4:
				if C==0 or g[B][C-1]!=4:
					A=1
					while C+A<J and g[B][C+A]==4:A+=1
					if A>1:G.append((B,C,0,1,A))
				if B==0 or g[B-1][C]!=4:
					A=1
					while B+A<I and g[B+A][C]==4:A+=1
					if A>1:G.append((B,C,1,0,A))
	for K in range(len(G)):
		for U in range(K+1,len(G)):
			V,W,D,E,L=G[K];M,N,X,Y,Z=G[U]
			if D==X and E==Y and L==Z:
				for O in range(I):
					for P in range(J):
						H=g[O][P]
						if H and H!=4:
							Q,R=O-V,P-W;F=Q*D+R*E
							if 0<=F<L:
								S,T=Q-F*D,R-F*E
								if(S,T)==(E,-D):g[M+F*D-E][N+F*E+D]=H
								if(S,T)==(-E,D):g[M+F*D+E][N+F*E-D]=H
				return g
	return g