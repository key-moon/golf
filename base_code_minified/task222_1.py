def p(g):
	H={}
	for(E,C)in enumerate(g):
		for(F,D)in enumerate(C):
			if D:H.setdefault(D,[]).append((E,F))
	A=[0,0,0,0,0,0]
	for(D,B)in H.items():
		I,J=min(A[0]for A in B),max(A[0]for A in B);K,L=min(A[1]for A in B),max(A[1]for A in B);G=(J-I+1)*(L-K+1)
		if G==len(B)and G>A[0]:A=[G,I,K,J,L,D]
	C=[[0]*len(g[0])for A in g]
	for E in range(A[1],A[3]+1):
		for F in range(A[2],A[4]+1):C[E][F]=A[5]
	return C