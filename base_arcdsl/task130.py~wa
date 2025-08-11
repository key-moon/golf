def Z(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def P(A,B):
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
def p(I):I=tuple(map(tuple,I));A=Z(I,5,0);B=P(A,3);return[*map(list,B)]