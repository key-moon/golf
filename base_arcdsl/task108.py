def X(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def P(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def E(A,C):
	if len(A)==0:return A
	B,D=C
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C+B,E+D))for(A,(C,E))in A)
	return frozenset((A+B,C+D)for(A,C)in A)
def S(A):return tuple(map(min,zip(*P(A))))
def Z(A,B):
	E,I=len(A),len(A[0]);C=tuple()
	for D in range(E):
		F=tuple()
		for H in range(I):
			if H%B==0:F=F+(A[D][H],)
		C=C+(F,)
	E=len(C);G=tuple()
	for D in range(E):
		if D%B==0:G=G+(C[D],)
	return G
def J(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for J in A:
			D=tuple()
			for F in J:D=D+tuple(F for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		G,H=S(A);K,L=-G,-H;M=E(A,(K,L));I=set()
		for(F,(N,O))in M:
			for P in range(B):
				for Q in range(B):I.add((F,(N*B+P,O*B+Q)))
		return E(frozenset(I),(G,H))
def U(A):return tuple(tuple(A[::-1])for A in A[::-1])
def p(I):I=tuple(map(tuple,I));A=U(I);B=Z(A,2);C=U(B);D=J(C,4);return[*map(list,D)]