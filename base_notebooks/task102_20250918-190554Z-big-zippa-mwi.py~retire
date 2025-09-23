def p(g):
	E,F=len(g),len(g[0]);K={};[[K.update({A:K.get(A,0)+1})for A in A]for A in g];S=max(K,key=K.get);L=[[0]*F for A in range(E)];Q=[]
	for C in range(E):
		for D in range(F):
			if not L[C][D]and g[C][D]!=S:
				A=[];G=[(C,D)];T=g[C][D]
				while G:
					H,I=G.pop()
					if 0<=H<E and 0<=I<F and not L[H][I]and g[H][I]==T:L[H][I]=1;A.append((H,I));G.extend([(H+A,I+B)for(A,B)in[(0,1),(1,0),(0,-1),(-1,0)]])
				A and Q.append(A)
	R=[]
	for A in Q:
		if A:M,N,O,P=min(A[0]for A in A),max(A[0]for A in A),min(A[1]for A in A),max(A[1]for A in A);U=set((A,B)for A in range(M,N+1)for B in range(O,P+1));B=list(U-set(A));B and R.append(B)
	G=[]
	for B in R:
		if B:M,N,O,P=min(A[0]for A in B),max(A[0]for A in B),min(A[1]for A in B),max(A[1]for A in B);E,F=N-M+1,P-O+1;E==F and len(B)==E*F and G.extend(B)
	J=[A[:]for A in g]
	for(C,D)in G:0<=C<len(J)and 0<=D<len(J[0])and J.__setitem__(C,J[C][:D]+[2]+J[C][D+1:])
	return J