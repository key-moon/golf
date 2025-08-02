def p(A):
	B=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==5];F=sum(A for(A,B)in B);G=sum(A for(B,A)in B);C=len(B)
	for(D,E)in B:A[D][E]=8 if(D*C-F)*(E*C-G)>0 else 2
	return A