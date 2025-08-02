def p(A):
	F=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D];(G,H),(I,J)=F;B,C=(G+I)//2,(H+J)//2
	for(D,E)in((B,C),(B-1,C),(B+1,C),(B,C-1),(B,C+1)):
		if 0<=D<len(A)and 0<=E<len(A[0]):A[D][E]=3
	return A