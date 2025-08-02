def p(A):
	I={A for B in A for A in B if A};J={}
	for C in I:P=[(A,D)for(A,B)in enumerate(A)for(D,E)in enumerate(B)if E==C];Q=[A[0]for A in P];R=[A[1]for A in P];J[C]=[min(Q),max(Q),min(R),max(R)]
	def W(A):B,C,D,E=val_b[A];return all(val_g[B][C]==A for B in range(B,C+1)for C in range(D,E+1))
	for C in I:
		if W(C):S=C
	B=(I-{S}).pop();K,L=len(A),len(A[0]);E=[(D,C)for D in range(K)for C in range(L)if A[D][C]==B and(C>0 and A[D][C-1]==B or C<L-1 and A[D][C+1]==B)];F=[(C,D)for C in range(K)for D in range(L)if A[C][D]==B and(C>0 and A[C-1][D]==B or C<K-1 and A[C+1][D]==B)];T,U,X,V=J[S];Y,Z,a,b=J[B]
	if U<Y:G=U+1-min(A for(A,B)in E);H=0;D=E
	elif T>Z:G=T-1-max(A for(A,B)in E);H=0;D=E
	elif V<a:H=V+1-min(A for(B,A)in F);G=0;D=F
	else:H=X-1-max(A for(B,A)in F);G=0;D=F
	M=[A[:]for A in A]
	for(N,O)in D:M[N][O]=0
	for(N,O)in D:M[N+G][O+H]=B
	return M