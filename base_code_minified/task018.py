def p(A):
	from collections import deque;P,H=len(A),len(A[0]);I=[[0]*H for A in A];Q=[]
	for J in range(P):
		for K in range(H):
			if A[J][K]and not I[J][K]:
				N=deque([(J,K)]);I[J][K]=1;R=[]
				while N:
					B,C=N.popleft();R.append((B,C))
					for(U,V)in((1,0),(-1,0),(0,1),(0,-1)):
						D,E=B+U,C+V
						if 0<=D<P and 0<=E<H and A[D][E]and not I[D][E]:I[D][E]=1;N.append((D,E))
				Q.append(R)
	def S(A):B=[A for(A,B)in A];C=[A for(B,A)in A];return max(B)-min(B),max(C)-min(C)
	O=[A for A in Q if S(A)[0]>S(A)[1]][0];L=[A for(A,B)in O];M=[A for(B,A)in O];Y,Z,F=min(L),max(L),(min(L)+max(L))/2;a,b,G=min(M),max(M),(min(M)+max(M))/2;W=[(A-F,B-G)for(A,B)in O];X=[(int(F+(B-G)),int(G-(A-F)))for(A,B)in W];T=[[0]*H for A in A]
	for(B,C)in X:T[B][C]=A[int(F+B-F)][int(G+C-G)]
	return T