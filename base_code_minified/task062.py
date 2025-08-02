import sys
def p(A):
	B=len(A);C=[(C,D,A[C][D])for C in range(B)for D in range(B)if A[C][D]>1]
	if not C:return[[3]*B for A in A]
	D=max(A for(*B,A)in C);F=[A for(A,C,B)in C if B==D];G,H=min(F),max(F);I=[A for(C,A,B)in C if B==D];J,K=min(I),max(I);L=(G+H)//2;M=(J+K)//2;E=[[3]*B for A in A]
	for N in range(J,K+1):E[L][N]=D
	for O in range(G,H+1):E[O][M]=D
	return E
if __name__=='__main__':
	g=[list(map(int,A.split()))for A in sys.stdin]
	for row in p(g):print(*row)