def p(g):
	O,P=len(g),len(g[0]);Q={A for B in g for A in B if A};E={A:sum(B.count(A)for B in g)for A in Q};B,K=max(E,key=E.get),min(E,key=E.get);X=min(A for(A,C)in enumerate(g)for(E,D)in enumerate(C)if D==B);Y=max(A for(A,C)in enumerate(g)for(E,D)in enumerate(C)if D==B);Z=min(C for A in g for(C,D)in enumerate(A)if D==B);a=max(C for A in g for(C,D)in enumerate(A)if D==B);L,R,M,S=X+1,Y,Z+1,a;b=[(A-L,B-M)for A in range(L,R)for B in range(M,S)if g[A][B]==K];c,d=R-L,S-M;T=[A for A in Q if A not in(B,K)];U=T[0]if T else None;F=set()
	for G in range(O):
		for H in range(P):
			if g[G][H]==U and(G,H)not in F:
				N=[(G,H)];A=[];F.add((G,H))
				while N:
					I,J=N.pop();A.append((I,J))
					for(e,f)in((1,0),(-1,0),(0,1),(0,-1)):
						C,D=I+e,J+f
						if 0<=C<O and 0<=D<P and g[C][D]==U and(C,D)not in F:F.add((C,D));N.append((C,D))
				V,h=min(A for(A,B)in A),max(A for(A,B)in A);W,i=min(A for(B,A)in A),max(A for(B,A)in A)
				if h-V+1==c and i-W+1==d and set((A-V,B-W)for(A,B)in A)==set(b):
					for(I,J)in A:g[I][J]=K
	return g