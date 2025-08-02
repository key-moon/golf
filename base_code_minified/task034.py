def p(A):
	D=9
	for B in range(D):
		for C in range(D):
			if A[B][C]==2:I,J=B,C
	for(E,F)in((1,0),(0,1),(-1,0),(0,-1)):
		B,C=I+E,J+F
		if 0<=B<D and 0<=C<D and A[B][C]>2:H=A[B][C];G=E,F
	for(E,F)in((1,0),(0,1),(-1,0),(0,-1)):
		if(E,F)==G or(E,F)==(-G[0],-G[1]):continue
		B,C=I+E,J+F
		if 0<=B<D and 0<=C<D and A[B][C]>2:K=E,F
	A[I][J]=H
	while True:
		L=False
		for B in range(D):
			for C in range(D):
				if A[B][C]==0:
					M,N=B-G[0],C-G[1];O,P=B-K[0],C-K[1]
					if 0<=M<D and 0<=N<D and 0<=O<D and 0<=P<D:
						if A[M][N]==H and A[O][P]==H:A[B][C]=H;L=True
		if not L:break
	return A