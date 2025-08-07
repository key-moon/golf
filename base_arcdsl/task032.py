def Z(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def S(A):return tuple(A for A in zip(*A[::-1]))
def U(A,B):return type(B)(A(B)for B in B)
def J(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def E(A,B):return tuple(sorted(A,key=B))
def P(x):return x
def p(I):I=tuple(map(tuple,I));A=Z(I);B=J(E,P);C=U(B,A);D=S(C);return[*map(list,D)]