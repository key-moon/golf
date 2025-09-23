def p(M):
	G,H=len(M),len(M[0]);D=[[0]*H for A in range(G)];L={}
	for A in range(G):
		for B in range(H):
			C=M[A][B]
			if C in(1,2):L[C]=A,B;D[A][B]=C
	R={3:L[2],7:L[1]}
	for A in range(G):
		for B in range(H):
			C=M[A][B]
			if C not in(0,1,2):
				E,F=R[C]
				if A==E:N=F+(1 if B>F else-1);D[A].__setitem__(N,C)if 0<=N<H and not D[A][N]else D[A].__setitem__(B,C)
				elif B==F:O=E+(1 if A>E else-1);D[O].__setitem__(B,C)if 0<=O<G and not D[O][B]else D[A].__setitem__(B,C)
				else:
					K,P=None,1e9
					for(I,J)in((E,F+1),(E,F-1),(E+1,F),(E-1,F)):
						if 0<=I<G and 0<=J<H and not D[I][J]and(I==A or J==B):
							Q=abs(A-I)+abs(B-J)
							if Q<P:P,K=Q,(I,J)
					D[K[0]].__setitem__(K[1],C)if K else D[A].__setitem__(B,C)
	return D