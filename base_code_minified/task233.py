def p(A):
	H={}
	for V in A:
		for D in V:
			if D:H[D]=H.get(D,0)+1
	I=max(H,key=H.get);K,L=len(A),len(A[0]);J=set();N=[]
	for B in range(K):
		for C in range(L):
			if A[B][C]==I and(B,C)not in J:
				O=[(B,C)];J.add((B,C));E=[]
				for(P,Q)in O:
					E.append((P,Q))
					for(W,X)in((1,0),(-1,0),(0,1),(0,-1)):
						F,G=P+W,Q+X
						if 0<=F<K and 0<=G<L and A[F][G]==I and(F,G)not in J:J.add((F,G));O.append((F,G))
				N.append(E)
	E=max(N,key=len);R=[A for(A,B)in E];S=[A for(B,A)in E];r0,r1,min(R),max(R);M,T=min(S),max(S);Y=r1-r0+1;Z=T-M+1;U=[[I]*Z for A in range(Y)]
	for B in range(K):
		for C in range(L):
			D=A[B][C]
			if D and D!=I and r0<=B<=r1 and M<=C<=T:U[B-r0][C-M]=D
	return U