def p(g):
	A=[];J=len(g);K=len(g[0])
	for H in range(J):
		for I in range(K):
			if g[H][I]==8:
				B=[H,I];g[H][I]=0;E=0
				while E<len(B):
					C,D=B[E],B[E+1];E+=2
					for(L,M)in((1,0),(-1,0),(0,1),(0,-1)):
						F,G=C+L,D+M
						if 0<=F<J and 0<=G<K and g[F][G]==8:g[F][G]=0;B+=[F,G]
				A.append(B)
	A.sort(key=len)
	for(C,D)in zip(A[-1][::2],A[-1][1::2]):g[C][D]=1
	for(C,D)in zip(A[0][::2],A[0][1::2]):g[C][D]=2
	return g