def p(g):
	I=[];J=1,0,-1,0,1
	for F in range(10):
		for G in range(10):
			if g[F][G]==5:
				H=[(F,G)];g[F][G]=0;A=[]
				while H:
					B,C=H.pop();A.append((B,C))
					for K in range(4):
						D=B+J[K];E=C+J[K+1]
						if 0<=D<10 and 0<=E<10 and g[D][E]==5:g[D][E]=0;H.append((D,E))
				I.append(A)
	for(A,L)in zip(sorted(I,key=len,reverse=True),(1,4,2)):
		for(B,C)in A:g[B][C]=L
	return g