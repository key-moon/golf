def p(g,R=enumerate):
	A,B=[(A,C)for(A,B)in R(g)for(C,D)in R(B)if D==2],[(A,C)for(A,B)in R(g)for(C,D)in R(B)if D==8]
	if not A or not B:return g
	E=lambda s:(min(A for(A,B)in s),max(A for(A,B)in s),min(A for(B,A)in s),max(A for(B,A)in s));F,G,H,I=E(A);J,K,L,M=E(B);C=D=0
	if I<L:D=L-I-1
	elif M<H:D=M-H+1
	elif G<J:C=J-G-1
	elif K<F:C=K-F+1
	N,O={*A},{*B};return[[8 if(A,B)in O else 2 if(A-C,B-D)in N else 0 for(B,E)in R(g[0])]for(A,B)in R(g)]