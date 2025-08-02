def p(g):
	K,L=len(g),len(g[0]);B={(A,B)for A in range(K)for B in range(L)if g[A][B]}
	while B:
		A=[B.pop()]
		for P in A:
			C,D=P
			for(E,F)in((1,0),(-1,0),(0,1),(0,-1)):
				G=C+E,D+F
				if G in B:B.remove(G);A.append(G)
		if len(A)>1:
			H={}
			for(C,D)in A:H[g[C][D]]=H.get(g[C][D],0)+1
			for(M,Q)in H.items():
				if Q==1:break
			N,O=[(A,B)for(A,B)in A if g[A][B]==M][0];R=[(A-N,B-O,g[A][B])for(A,B)in A]
			for I in range(K):
				for J in range(L):
					if g[I][J]==M and(I,J)!=(N,O):
						for(E,F,S)in R:g[I+E][J+F]=S
	return g