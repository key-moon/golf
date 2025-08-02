def p(g):
	C={};B={}
	for(D,N)in enumerate(g):
		for(E,A)in enumerate(N):
			C[A]=C.get(A,0)+1
			if A in B:F,G,H,I=B[A];B[A]=[min(F,D),min(G,E),max(H,D),max(I,E)]
			else:B[A]=[D,E,D,E]
	O=max(C,key=C.get);K=[]
	for(A,(F,G,H,I))in B.items():
		if A==O:continue
		L=H-F+1;M=I-G+1
		if L%2 and M%2:K.append((L*M,-A,F,H,G,I))
	J=max(K);return[A[J[4]:J[5]+1]for A in g[J[2]:J[3]+1]]