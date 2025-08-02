def p(g):
	B=[(A,C)for(A,B)in enumerate(g)for(C,D)in enumerate(B)if D==5];A=max(B,key=lambda a:max((a[0]-A[0])**2+(a[1]-A[1])**2 for A in B));C=max(B,key=lambda b:(A[0]-b[0])**2+(A[1]-b[1])**2)
	for(D,E)in B:g[D][E]=8 if(C[0]-A[0])*(E-A[1])-(C[1]-A[1])*(D-A[0])<=0 else 2
	return g