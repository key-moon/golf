def p(g):
	B,S=len(g),len(g[0]);G=next(A for B in g for A in B if A);E=[tuple(A for(A,B)in enumerate(A)if B==G)for A in g];K=0
	for H in range(1,B):
		if B>=2*H and all(E[A]==E[A+H]for A in range(B-H)):K=H;break
	I=[[0]*S for A in range(10)]
	for A in range(B):
		for C in E[A]:I[A][C]=G
	if K:
		for A in range(B,10):
			for C in E[A-K]:I[A][C]=G
	else:
		J={(A,B)for A in range(B)for B in E[A]};L={A:[]for A in J}
		for(A,C)in J:
			for(X,Y)in((1,0),(-1,0),(0,1),(0,-1)):
				T=A+X,C+Y
				if T in J:L[A,C].append(T)
		U=[A for A in J if len(L[A])==1];Z,V=min(U),max(U)
		def W(u,p):
			if u==V:return[u]
			for A in L[u]:
				if A!=p:
					B=W(A,u)
					if B:return[u]+B
		F=W(Z,None);D=[(F[A+1][0]-F[A][0],F[A+1][1]-F[A][1])for A in range(len(F)-1)]
		for M in range(1,len(D)+1):
			if all(D[A]==D[A+M]for A in range(len(D)-M)):N=D[:M];break
		O=len(D)%len(N);P=V
		while True:
			a,b=N[O];Q,R=P[0]+a,P[1]+b
			if not(0<=Q<10 and 0<=R<S):break
			I[Q][R]=G;P=Q,R;O=(O+1)%len(N)
	return I