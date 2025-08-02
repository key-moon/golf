def p(val_g):
	H=val_g;R,S=len(H),len(H[0]);I={}
	for C in range(R):
		for D in range(S):
			A=H[C][D]
			if A:I.setdefault(A,[]).append((D,C))
	E=[];F=[]
	for(A,T)in I.items():
		M,N=zip(*T);J,U,K,V=min(M),max(M),min(N),max(N);O,P=U-J,V-K
		if O and P:Q,W,X,Y=A,J,K,O+1
		elif P==0:E.append((K,A))
		else:F.append((J,A))
	E.sort();F.sort();Z=E[0][1];a=E[-1][1];b=F[0][1];c=F[-1][1];L=Y+2;B=[[0]*L for A in range(L)]
	for G in range(1,L-1):B[0][G]=Z;B[-1][G]=a;B[G][0]=b;B[G][-1]=c
	for(D,C)in I[Q]:B[C-X+1][D-W+1]=Q
	return B