def p(A):
	D={};C={}
	for(E,O)in enumerate(A):
		for(F,B)in enumerate(O):
			D[B]=D.get(B,0)+1
			if B in C:G,H,I,J=C[B];C[B]=[min(G,E),min(H,F),max(I,E),max(J,F)]
			else:C[B]=[E,F,E,F]
	P=max(D,key=D.get);L=[]
	for(B,(G,H,I,J))in C.items():
		if B==P:continue
		M=I-G+1;N=J-H+1
		if M%2 and N%2:L.append((M*N,-B,G,I,H,J))
	K=max(L);return[A[K[4]:K[5]+1]for A in A[K[2]:K[3]+1]]