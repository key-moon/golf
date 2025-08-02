def p(A):
	E={}
	for(Q,R)in enumerate(A):
		for(S,F)in enumerate(R):
			if F:E.setdefault(F,[]).append((Q,S))
	T=sorted(E.items(),key=lambda H:min(A for(B,A)in H[1]));G=[]
	for(U,H)in T:I,J=zip(*H);K,L=min(I),min(J);V,W=max(I)-K+1,max(J)-L+1;G.append((U,[(A-K,B-L)for(A,B)in H],V,W))
	(X,M,Y,Y),(Z,N,a,b)=G;c=set(M)
	for(O,P)in((0,3-b),(3-a,0)):
		if all((A+O,B+P)not in c for(A,B)in N):break
	B=[[0]*3 for A in range(3)]
	for(C,D)in M:B[C][D]=X
	for(C,D)in N:B[C+O][D+P]=Z
	return B