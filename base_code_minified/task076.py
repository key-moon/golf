def p(g):
	D,E=len(g),len(g[0]);F=lambda v:(v[1],-v[0]);H=[];M=[[0]*E for A in range(D)]
	for B in range(D):
		for C in range(E):
			if g[B][C]==4 and not M[B][C]:
				if C+1<E and g[B][C+1]==4:
					G=[];A=C
					while A<E and g[B][A]==4:M[B][A]=1;G.append((B,A));A+=1
					H.append((G,(0,1)))
				elif B+1<D and g[B+1][C]==4:
					G=[];A=B
					while A<D and g[A][C]==4:M[A][C]=1;G.append((A,C));A+=1
					H.append((G,(1,0)))
	N,I=H[0];T=len(N);J,K=F(I),(-F(I)[0],-F(I)[1]);U=[g[A+J[0]][B+J[1]]if 0<=A+J[0]<D and 0<=B+J[1]<E else 0 for(A,B)in N];V=[g[A+K[0]][B+K[1]]if 0<=A+K[0]<D and 0<=B+K[1]<E else 0 for(A,B)in N]
	for(W,L)in H:
		R=0;O=L
		for b in range(4):
			if O==I:break
			O=F(O);R+=1
		for(A,(X,Y))in enumerate(W):
			for(c,(Z,S))in enumerate(((U,F(L)),(V,(-F(L)[0],-F(L)[1])))):
				P,Q=X+S[0],Y+S[1]
				if 0<=P<D and 0<=Q<E and g[P][Q]==0:a=A if R!=2 else T-1-A;g[P][Q]=Z[a]
	return g