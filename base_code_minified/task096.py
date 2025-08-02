def p(A):
	R,S=len(A),len(A[0]);N={}
	for d in A:
		for B in d:N[B]=N.get(B,0)+1
	G=max(N,key=N.get);O=[[0]*S for A in range(R)];H=[]
	for D in range(R):
		for F in range(S):
			if A[D][F]!=G and not O[D][F]:
				Y=A[D][F];T=[(D,F)];O[D][F]=1;Z=[];P,U,Q,V=D,D,F,F
				while T:
					C,B=T.pop();Z.append((C,B))
					if C<P:P=C
					if C>U:U=C
					if B<Q:Q=B
					if B>V:V=B
					for(e,f)in((1,0),(-1,0),(0,1),(0,-1)):
						I,J=C+e,B+f
						if 0<=I<R and 0<=J<S and not O[I][J]and A[I][J]==Y:O[I][J]=1;T.append((I,J))
				K=U-P+1;L=V-Q+1;E=K if K>L else L;W=[[G]*L for A in range(K)]
				for(C,B)in Z:W[C-P][B-Q]=Y
				g=E-K;h=E-L;i=g//2;j=h//2;M=[[G]*E for A in range(E)]
				for C in range(K):
					for B in range(L):
						if W[C][B]!=G:M[i+C][j+B]=W[C][B]
				H.append((E,M))
	H.sort(key=lambda F:F[0]);a=len(H)-1;X=H[0][0]+2*a;k=X//2;b=[[G]*X for A in range(X)]
	for(D,(E,M))in enumerate(H):
		l=a-D;c=k-E//2-l
		for C in range(E):
			for B in range(E):
				if M[C][B]!=G:b[c+C][c+B]=M[C][B]
	return b