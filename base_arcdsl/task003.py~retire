def P(A):return A[len(A)//2+len(A)%2:]
def S(A):return A[:len(A)//2]
def U(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def J(a,b):return a+b
def X(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def E(A,a,b):return a if A else b
def Z(a,b):return a==b
def p(I):I=tuple(map(tuple,I));B=S(I);A=P(I);C=Z(B,A);D=X(I,(2,0),(3,3));F=E(C,A,D);G=J(I,F);H=U(G,1,2);return[*map(list,H)]