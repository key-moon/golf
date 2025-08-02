def p(A):
	E={}
	for(C,J)in enumerate(A):
		for(D,F)in enumerate(J):
			if F:E.setdefault(F,[]).append((C,D))
	G=[[0]*4 for A in[0]*4]
	for(K,B)in E.items():
		H=min(A for(A,B)in B);I=min(A for(B,A)in B);L=sum(A for(A,B)in B);M=sum(A for(B,A)in B);N=L-1-3*H;O=M-1-3*I
		for(C,D)in B:G[N*2+C-H][O*2+D-I]=K
	return G