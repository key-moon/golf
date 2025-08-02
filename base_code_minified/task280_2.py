def p(A):
	H=len(A);I=len(A[0]);L=[A[:]for A in A]
	for B in range(H):
		for C in range(I):
			if A[B][C]==2:
				D=B
				while D and A[D-1][C]==3:D-=1
				E=B
				while E<H-1 and A[E+1][C]==3:E+=1
				F=C
				while F and A[B][F-1]==3:F-=1
				G=C
				while G<I-1 and A[B][G+1]==3:G+=1
				J=(B==D)*-1+(B==E);K=(C==F)*-1+(C==G);P=J and(B if J<0 else H-1-B)or K and(C if K<0 else I-1-C)
				for M in range(1,P+1):
					for N in range(D,E+1):
						for O in range(F,G+1):L[N+J*M][O+K*M]=A[N][O]
	return L