def p(val_g):
	A=val_g;J={A for B in A for A in B if A};E={}
	for C in J:P=[(A,D)for(A,B)in enumerate(A)for(D,E)in enumerate(B)if E==C];Q=[A[0]for A in P];R=[A[1]for A in P];E[C]=[min(Q),max(Q),min(R),max(R)]
	def W(c):B,C,D,F=E[c];return all(A[B][C]==c for B in range(B,C+1)for C in range(D,F+1))
	for C in J:
		if W(C):S=C
	B=(J-{S}).pop();K,L=len(A),len(A[0]);F=[(D,C)for D in range(K)for C in range(L)if A[D][C]==B and(C>0 and A[D][C-1]==B or C<L-1 and A[D][C+1]==B)];G=[(C,D)for C in range(K)for D in range(L)if A[C][D]==B and(C>0 and A[C-1][D]==B or C<K-1 and A[C+1][D]==B)];T,U,X,V=E[S];Y,Z,a,b=E[B]
	if U<Y:H=U+1-min(A for(A,B)in F);I=0;D=F
	elif T>Z:H=T-1-max(A for(A,B)in F);I=0;D=F
	elif V<a:I=V+1-min(A for(B,A)in G);H=0;D=G
	else:I=X-1-max(A for(B,A)in G);H=0;D=G
	M=[A[:]for A in A]
	for(N,O)in D:M[N][O]=0
	for(N,O)in D:M[N+H][O+I]=B
	return M