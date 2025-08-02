def p(A):
	C=len(A);E=len(A[0])
	for B in range(C):
		if A[B][0]and all(C==A[B][0]for C in A[B]):J=A[B][0];break
	K=[B for B in range(C)if all(A==J for A in A[B])];L=[B for B in range(E)if all(A[C][B]==J for C in range(C))];H=[-1]*C
	for B in range(len(K)-1):
		for T in range(K[B]+1,K[B+1]):H[T]=B
	I=[-1]*E
	for B in range(len(L)-1):
		for U in range(L[B]+1,L[B+1]):I[U]=B
	D=[(H[B],I[C],A[B][C])for B in range(C)for C in range(E)if A[B][C]!=0 and A[B][C]!=J]
	for M in{A[0]for A in D}:
		F=[A[2]for A in D if A[0]==M]
		if len({*F})==1:
			N=F[0];R=[A[1]for A in D if A[0]==M];O,P=min(R),max(R)
			for B in range(C):
				if H[B]==M:
					for G in range(E):
						if O<=I[G]<=P:A[B][G]=N
	for Q in{A[1]for A in D}:
		F=[A[2]for A in D if A[1]==Q]
		if len({*F})==1:
			N=F[0];S=[A[0]for A in D if A[1]==Q];O,P=min(S),max(S)
			for G in range(E):
				if I[G]==Q:
					for B in range(C):
						if O<=H[B]<=P:A[B][G]=N
	return A