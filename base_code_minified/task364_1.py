def p(g):
	K,G=len(g),len(g[0]);D=[[0]*G for A in g];H=[]
	for E in range(K):
		for F in range(G):
			if g[E][F]==3 and not D[E][F]:
				A=[(E,F)];D[E][F]=1
				for(I,J)in A:
					for(L,M)in((1,0),(-1,0),(0,1),(0,-1)):
						B,C=I+L,J+M
						if 0<=B<K and 0<=C<G and g[B][C]==3 and not D[B][C]:D[B][C]=1;A.append((B,C))
				H.append(A)
	N=sorted({len(A)for A in H});O={A:B for(A,B)in zip(N,(1,2,6))}
	for A in H:
		for(I,J)in A:g[I][J]=O[len(A)]
	return g