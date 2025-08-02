def p(g):
	J={A for B in g for A in B if A};A,G=J;K=[(-1,-1),(-1,1),(1,-1),(1,1)];B=lambda L:max(sum((A+C,B+D)in L for(C,D)in K)for(A,B)in L);C=[(B,D)for(B,C)in enumerate(g)for(D,E)in enumerate(C)if E==A];D=[(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==G]
	if B(C)>B(D):E,L=D,A
	else:E,L=C,F=G=A and A
	if B(C)>B(D):E=C;F=G
	else:E=D;F=A
	H=[(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==F];M=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)];I=max(H,key=lambda p:sum((p[0]+A,p[1]+B)in H for(A,B)in M));N=[(A-I[0],B-I[1])for(A,B)in H]
	for(O,P)in E:
		for(Q,R)in N:g[O+Q][P+R]=F
	return g