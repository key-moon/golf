def p(A):
	C={}
	for(D,E)in enumerate(A):
		for(F,B)in enumerate(E):
			if B:C[B]=min(C.get(B,len(A)),D)
	H=C[1];G=[[0]*len(A)for A in A]
	for(D,E)in enumerate(A):
		for(F,B)in enumerate(E):
			if B:G[D-C[B]+H][F]=B
	return G