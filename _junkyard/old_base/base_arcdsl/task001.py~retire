def P(a,b,A):
	G,H=len(a),len(a[0]);B=tuple()
	for D in range(G):
		C=tuple()
		for E in range(H):F=a[D][E];I=F if F==b[D][E]else A;C=C+(I,)
		B=B+(C,)
	return B
def J(a,b):return a+b
def U(a,b):return tuple(A+B for(A,B)in zip(a,b))
def S(A,B):
	C=tuple()
	for D in A:C=C+tuple(D for A in range(B))
	return C
def Z(A,B):
	C=tuple()
	for E in A:
		D=tuple()
		for F in E:D=D+tuple(F for A in range(B))
		C=C+(D,)
	return C
def p(I):I=tuple(map(tuple,I));B=Z(I,3);C=S(B,3);D=U(I,I);A=U(D,I);E=J(A,A);F=J(E,A);G=P(C,F,0);return[*map(list,G)]