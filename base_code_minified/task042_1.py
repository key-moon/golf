def p(g):
	H,I=len(g),len(g[0]);S=[(A,B)for A in range(H)for B in range(I)if g[A][B]==3];F=set();M=[]
	for(J,K)in S:
		if(J,K)in F:continue
		L=[(J,K)];A=[];F.add((J,K))
		while L:
			B,C=L.pop();A.append((B,C))
			for(T,U)in[(1,0),(-1,0),(0,1),(0,-1)]:
				D,E=B+T,C+U
				if 0<=D<H and 0<=E<I and(D,E)not in F and g[D][E]==3:F.add((D,E));L.append((D,E))
		M.append(A)
	G=[];N=[]
	for A in M:V=[A for(A,B)in A];W=[A for(B,A)in A];O,P=min(V),min(W);G.append((O,P));N.append([(A-O,B-P)for(A,B)in A])
	X=sorted({A for(A,B)in G});Y=sorted({A for(B,A)in G})
	for Q in X:
		for R in Y:
			if(Q,R)in G:continue
			for Z in N:
				for(a,b)in Z:
					B,C=Q+a,R+b
					if 0<=B<H and 0<=C<I and g[B][C]==0:g[B][C]=8
	return g