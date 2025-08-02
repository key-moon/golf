def p(A):
	C=[(A,C)for(A,B)in enumerate(A)for(C,D)in enumerate(B)if D==5];B=max(C,key=lambda H:max((H[0]-A[0])**2+(H[1]-A[1])**2 for A in C));D=max(C,key=lambda I:(B[0]-I[0])**2+(B[1]-I[1])**2)
	for(E,F)in C:A[E][F]=8 if(D[0]-B[0])*(F-B[1])-(D[1]-B[1])*(E-B[0])<=0 else 2
	return A