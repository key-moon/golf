def p(val_g):
	A=val_g;B={}
	for G in A:
		for C in G:B[C]=B.get(C,0)+1
	I=sorted(B,key=B.get,reverse=1);N,H=I[1],I[2];D=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==N];J=min(A for(A,B)in D);K=max(A for(A,B)in D);L=min(A for(B,A)in D);M=max(A for(B,A)in D)
	for(E,G)in enumerate(A):
		for(F,C)in enumerate(G):
			if C==H:
				if J<=E<=K:
					for O in range(min(F,L),max(F,M)+1):A[E][O]=H
				if L<=F<=M:
					for P in range(min(E,J),max(E,K)+1):A[P][F]=H
	return A