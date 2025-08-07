def L(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def Y(A):return tuple(A for A in zip(*A[::-1]))
def S(A):return L(Z(Y(A)))
def J(A):return L(E(Y(A)))
def Z(A):return A[len(A)//2+len(A)%2:]
def E(A):return A[:len(A)//2]
def X(a,b):return a,b
def P(A):return min(set(A),key=A.count)
def U(a,b):return type(a)((*a,*b))
def p(I):I=tuple(map(tuple,I));A=J(I);B=S(I);C=E(A);D=E(B);F=Z(A);G=Z(B);H=X(C,D);K=X(F,G);L=U(H,K);M=P(L);return[*map(list,M)]