def p(A):
	G=len(A);I=len(A[0]);H=0
	for B in range(G):
		for D in range(B,G):
			C=0
			for F in range(I):
				if all(A[B][F]==0 for B in range(B,D+1)):
					C+=1
					if C*(D-B+1)>H:H=C*(D-B+1);E=B,D,F-C+1,F
				else:C=0
	for J in range(E[0],E[1]+1):
		for K in range(E[2],E[3]+1):A[J][K]=6
	return A