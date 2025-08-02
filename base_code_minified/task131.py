def p(g):
	try:A=next(B for(B,A)in enumerate(g)if A.count(2)==len(A));J='r'
	except:A=next(A for A in range(len(g[0]))if all(B[A]==2 for B in g));J='c'
	B=[(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==3];F=min(A for(A,B)in B);K=max(A for(A,B)in B);G=min(A for(B,A)in B);L=max(A for(B,A)in B);H=K-F+1;I=L-G+1
	if J=='c':
		if L<A:M=A-I-G;E=A-I-1
		else:M=A+1-G;E=A+1+I
		for(C,D)in B:g[C][D]=0;g[C][D+M]=3;g[C][E]=8
	else:
		if K<A:N=A-H-F;E=A-H-1
		else:N=A+1-F;E=A+1+H
		for(C,D)in B:g[C][D]=0;g[C+N][D]=3;g[E][D]=8
	return g