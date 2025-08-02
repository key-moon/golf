def p(val_g):
	A=val_g;M,H=len(A),len(A[0]);N=[[0]*H for A in A];I=[[0]*H for A in A]
	for J in range(M):
		for K in range(H):
			if A[J][K]==2 and not I[J][K]:
				L=[(J,K)];I[J][K]=1
				for(Q,R)in L:
					for(S,T)in((1,0),(-1,0),(0,1),(0,-1)):
						B,C=Q+S,R+T
						if 0<=B<M and 0<=C<H and A[B][C]==2 and not I[B][C]:I[B][C]=1;L.append((B,C))
				O=[A[0]for A in L];P=[A[1]for A in L];D,E,F,G=min(O),max(O),min(P),max(P)
				if E-D>1 and G-F>1 and all(A[D][B]==2 for B in range(F,G+1))and all(A[E][B]==2 for B in range(F,G+1))and all(A[B][F]==2 for B in range(D,E+1))and all(A[B][G]==2 for B in range(D,E+1)):
					for B in range(D+1,E):
						for C in range(F+1,G):N[B][C]=3
	return N