def p(g):
	G={}
	for U in g:
		for C in U:
			if C:G[C]=G.get(C,0)+1
	H=max(G,key=G.get);J,K=len(g),len(g[0]);I=set();M=[]
	for A in range(J):
		for B in range(K):
			if g[A][B]==H and(A,B)not in I:
				N=[(A,B)];I.add((A,B));D=[]
				for(O,P)in N:
					D.append((O,P))
					for(V,W)in((1,0),(-1,0),(0,1),(0,-1)):
						E,F=O+V,P+W
						if 0<=E<J and 0<=F<K and g[E][F]==H and(E,F)not in I:I.add((E,F));N.append((E,F))
				M.append(D)
	D=max(M,key=len);Q=[A for(A,B)in D];R=[A for(B,A)in D];r0,r1,min(Q),max(Q);L,S=min(R),max(R);X=r1-r0+1;Y=S-L+1;T=[[H]*Y for A in range(X)]
	for A in range(J):
		for B in range(K):
			C=g[A][B]
			if C and C!=H and r0<=A<=r1 and L<=B<=S:T[A-r0][B-L]=C
	return T