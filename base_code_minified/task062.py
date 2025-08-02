import sys
def p(g):
	A=len(g);B=[(B,C,g[B][C])for B in range(A)for C in range(A)if g[B][C]>1]
	if not B:return[[3]*A for B in g]
	C=max(A for(*B,A)in B);E=[A for(A,D,B)in B if B==C];F,G=min(E),max(E);H=[A for(D,A,B)in B if B==C];I,J=min(H),max(H);K=(F+G)//2;L=(I+J)//2;D=[[3]*A for B in g]
	for M in range(I,J+1):D[K][M]=C
	for N in range(F,G+1):D[N][L]=C
	return D
if __name__=='__main__':
	g=[list(map(int,A.split()))for A in sys.stdin]
	for row in p(g):print(*row)