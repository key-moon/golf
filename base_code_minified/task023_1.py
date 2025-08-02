def p(g):
	A=[(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==5];E=sum(A for(A,B)in A);F=sum(A for(B,A)in A);B=len(A)
	for(C,D)in A:g[C][D]=8 if(C*B-E)*(D*B-F)>0 else 2
	return g