def p(g):
	G=[[0]*len(g)for A in g];D,A=[(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==2],[(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==5];H=min(A for(A,B)in D);I=max(A for(A,B)in D);J=min(A for(B,A)in D);K=max(A for(B,A)in D)
	if max(A for(B,A)in A)-min(A for(B,A)in A)>=max(A for(A,B)in A)-min(A for(A,B)in A):
		for(B,C)in A:E=C-J;F=K-C;G[B][J-E if E<=F else K+F]=5
	else:
		for(B,C)in A:E=B-H;F=I-B;G[H-E if E<=F else I+F][C]=5
	for(B,C)in D:G[B][C]=2
	return G