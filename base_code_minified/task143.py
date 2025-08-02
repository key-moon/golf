import collections
def p(A):
	G,H=len(A),len(A[0]);F=[[0]*H for A in range(G)];O=[]
	for B in range(G):
		for C in range(H):
			if A[B][C]==5:O.append((B,C));F[B][C]=1
	P=O[:]
	for(K,L)in P:
		for(M,N)in((1,0),(-1,0),(0,1),(0,-1)):
			D,E=K+M,L+N
			if 0<=D<G and 0<=E<H and not F[D][E]and A[D][E]==5:F[D][E]=1;P.append((D,E))
	Q=collections.defaultdict(list)
	for B in range(G):
		for C in range(H):
			I=A[B][C]
			if I and I!=5 and not F[B][C]:
				J=[(B,C)];F[B][C]=1
				for(K,L)in J:
					for(M,N)in((1,0),(-1,0),(0,1),(0,-1)):
						D,E=K+M,L+N
						if 0<=D<G and 0<=E<H and not F[D][E]and A[D][E]==I:F[D][E]=1;J.append((D,E))
				T=min(A for(A,B)in J);U=min(A for(B,A)in J);R=tuple(sorted((A-T,B-U)for(A,B)in J));Q[R].append(I)
	for(R,S)in Q.items():
		if len(S)==2:
			I=max(S)
			for B in range(G):
				for C in range(H):
					if A[B][C]==I:A[B][C]=5
			return A
	return A