def p(A):
	D,S=len(A),len(A[0]);H=next(A for B in A for A in B if A);F=[tuple(A for(A,B)in enumerate(A)if B==H)for A in A];M=0
	for I in range(1,D):
		if D>=2*I and all(F[A]==F[A+I]for A in range(D-I)):M=I;break
	J=[[0]*S for A in range(10)]
	for B in range(D):
		for C in F[B]:J[B][C]=H
	if M:
		for B in range(D,10):
			for C in F[B-M]:J[B][C]=H
	else:
		K={(A,B)for A in range(D)for B in F[A]};T={A:[]for A in K}
		for(B,C)in K:
			for(X,Y)in((1,0),(-1,0),(0,1),(0,-1)):
				U=B+X,C+Y
				if U in K:T[B,C].append(U)
		V=[A for A in K if len(T[A])==1];Z,a=min(V),max(V)
		def W(A,B):
			if A==L:return[A]
			for D in C[A]:
				if D!=B:
					E=W(D,A)
					if E:return[A]+E
		G=W(Z,None);E=[(G[A+1][0]-G[A][0],G[A+1][1]-G[A][1])for A in range(len(G)-1)]
		for N in range(1,len(E)+1):
			if all(E[A]==E[A+N]for A in range(len(E)-N)):L=E[:N];break
		O=len(E)%len(L);P=a
		while True:
			b,c=L[O];Q,R=P[0]+b,P[1]+c
			if not(0<=Q<10 and 0<=R<S):break
			J[Q][R]=H;P=Q,R;O=(O+1)%len(L)
	return J