def p(g):
	K,L=len(g),len(g[0]);B={}
	for(M,N)in enumerate(g):
		for(O,A)in enumerate(N):
			if A:B.setdefault(A,[]).append((M,O))
	D=[[0]*L for A in range(K)]
	for(P,E)in B.items():
		if len(E)==1:
			F,A=E[0]
			for(Q,C)in B.items():
				if len(C)==4:
					G=sum(A==F for(A,B)in C);H=sum(B==A for(C,B)in C)
					if G and H and G+H==4:
						for(I,J)in((0,0),(-1,0),(1,0),(0,-1),(0,1)):D[F+I][A+J]=Q if I|J else P
	return D