def p(A):
	B=[];K=len(A);L=len(A[0])
	for I in range(K):
		for J in range(L):
			if A[I][J]==8:
				C=[I,J];A[I][J]=0;F=0
				while F<len(C):
					D,E=C[F],C[F+1];F+=2
					for(M,N)in((1,0),(-1,0),(0,1),(0,-1)):
						G,H=D+M,E+N
						if 0<=G<K and 0<=H<L and A[G][H]==8:A[G][H]=0;C+=[G,H]
				B.append(C)
	B.sort(key=len)
	for(D,E)in zip(B[-1][::2],B[-1][1::2]):A[D][E]=1
	for(D,E)in zip(B[0][::2],B[0][1::2]):A[D][E]=2
	return A