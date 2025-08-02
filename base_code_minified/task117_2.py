def p(A):
	G=len(A);H=len(A[0]);I=(G-1)/2;J=(H-1)/2;K={}
	for B in range(G):
		for C in range(H):
			if A[B][C]:K.setdefault(A[B][C],[]).append((B,C))
	for(L,D)in K.items():
		M=[A for(A,B)in D];N=[A for(B,A)in D];O,P=min(M),max(M);Q,R=min(N),max(N);S,T=(O+P)//2,(Q+R)//2
		if A[S][T]==L:
			for(B,C)in D:
				E=B-I;F=C-J
				for(U,V)in((-F,E),(-E,-F),(F,-E)):A[int(I+U)][int(J+V)]=L
	return A