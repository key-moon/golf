def p(g):
	N,O=len(g),len(g[0]);B=[A[:]for A in g]
	for D in{B for A in g for B in A}-{0}:
		A=[(A,C)for(A,B)in enumerate(g)for(C,E)in enumerate(B)if E==D];E=min(A for(A,B)in A);E=E;P=min(A for(B,A)in A);F=sum(A for(A,B)in A)/len(A);G=sum(A for(B,A)in A)/len(A);C=sorted(A,key=lambda p:-__import__('math').atan2(p[1]-G,p[0]-F));H=len(C)
		for(I,(J,K))in enumerate(C):L,M=C[(I+1)%H];B[L][M]=D;B[J][K]=0
	return B