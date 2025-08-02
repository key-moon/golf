def p(A):
	F,G=len(A),len(A[0]);H=set()
	for C in range(F):
		for B in range(G):
			D=A[C][B]
			if D:
				if C+1<F and(E:=A[C+1][B])!=D and E:H|={D,E}
				if B+1<G and(E:=A[C][B+1])!=D and E:H|={D,E}
	I=[(B,C)for B in range(F)for C in range(G)if A[B][C]in H];N=min(A for(A,B)in I);O=max(A for(A,B)in I);P=min(A for(B,A)in I);Q=max(A for(B,A)in I);J=[A[B][P:Q+1]for B in range(N,O+1)];K,E=len(J),len(J[0]);R={A for B in A for A in B if A and A not in H}
	for C in range(F-K+1):
		for B in range(G-E+1):
			D=A[C][B]
			if D in R and(C==0 or A[C-1][B]!=D)and(B==0 or A[C][B-1]!=D)and all(A[C+F][B:B+E]==[D]*E for F in range(K)):
				for L in range(K):
					for M in range(E):A[C+L][B+M]=J[L][M]
	return A