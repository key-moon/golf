def p(g):
	C=9
	for A in range(C):
		for B in range(C):
			if g[A][B]==2:H,I=A,B
	for(D,E)in((1,0),(0,1),(-1,0),(0,-1)):
		A,B=H+D,I+E
		if 0<=A<C and 0<=B<C and g[A][B]>2:G=g[A][B];F=D,E
	for(D,E)in((1,0),(0,1),(-1,0),(0,-1)):
		if(D,E)==F or(D,E)==(-F[0],-F[1]):continue
		A,B=H+D,I+E
		if 0<=A<C and 0<=B<C and g[A][B]>2:J=D,E
	g[H][I]=G
	while True:
		K=False
		for A in range(C):
			for B in range(C):
				if g[A][B]==0:
					L,M=A-F[0],B-F[1];N,O=A-J[0],B-J[1]
					if 0<=L<C and 0<=M<C and 0<=N<C and 0<=O<C:
						if g[L][M]==G and g[N][O]==G:g[A][B]=G;K=True
		if not K:break
	return g