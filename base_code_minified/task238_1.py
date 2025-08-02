def p(A):
	R,S=len(A),len(A[0]);I={}
	for D in range(R):
		for E in range(S):
			B=A[D][E]
			if B:I.setdefault(B,[]).append((E,D))
	F=[];G=[]
	for(B,T)in I.items():
		M,N=zip(*T);J,U,K,V=min(M),max(M),min(N),max(N);O,P=U-J,V-K
		if O and P:Q,W,X,Y=B,J,K,O+1
		elif P==0:F.append((K,B))
		else:G.append((J,B))
	F.sort();G.sort();Z=F[0][1];a=F[-1][1];b=G[0][1];c=G[-1][1];L=Y+2;C=[[0]*L for A in range(L)]
	for H in range(1,L-1):C[0][H]=Z;C[-1][H]=a;C[H][0]=b;C[H][-1]=c
	for(E,D)in I[Q]:C[D-X+1][E-W+1]=Q
	return C