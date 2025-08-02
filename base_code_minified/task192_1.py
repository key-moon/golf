def p(A):
	K=sum(A,[]);L=set(K)-{0};G=max(L,key=K.count);E,F=len(A),len(A[0]);B=[[G if A[B][C]==G else-1 for C in range(F)]for B in range(E)];H=[(C,A)for A in range(F)for C in(0,E-1)if B[C][A]==-1]+[(A,C)for A in range(E)for C in(0,F-1)if B[A][C]==-1]
	while H:
		C,D=H.pop();B[C][D]=-2
		for(M,N)in((1,0),(-1,0),(0,1),(0,-1)):
			I,J=C+M,D+N
			if 0<=I<E and 0<=J<F and B[I][J]==-1:H.append((I,J))
	for C in range(E):
		for D in range(F):
			if B[C][D]==-1:B[C][D]=G
			elif B[C][D]==-2:B[C][D]=0
	return B