def p(A):
	G,H=len(A),len(A[0]);I=[A[:]for A in A];J=[[0]*H for A in range(G)];Y=[(1,0),(-1,0),(0,1),(0,-1)];K=[]
	for L in range(G):
		for M in range(H):
			if A[L][M]and not J[L][M]:
				D=[(L,M)];J[L][M]=1
				for(Z,a)in D:
					for(O,P)in Y:
						E,F=Z+O,a+P
						if 0<=E<G and 0<=F<H and A[E][F]and not J[E][F]:J[E][F]=1;D.append((E,F))
				S,T=D[0];b=tuple(sorted((B-S,C-T,A[B][C])for(B,C)in D));K.append((b,D,S,T))
	Q={}
	for(B,R,C,C)in K:Q[B]=Q.get(B,0)+1
	for(B,R,C,C)in K:
		if Q[B]==2:N=B;c=[A for A in K if A[0]==B];break
	for(C,R,C,C)in c:
		for(d,e)in R:I[d][e]=0
	U=[A for(A,B,C)in N];V=[A for(B,A,C)in N];f=max(U)-min(U)+1;g=max(V)-min(V)+1
	for W in range(G-f+1):
		for X in range(H-g+1):
			if all(I[W+A][X+B]==0 for(A,B,C)in N):
				for(O,P,h)in N:I[W+O][X+P]=h
				return I