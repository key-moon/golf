def p(g):
	E=len(g);G={}
	for(R,S)in enumerate(g):
		for(T,H)in enumerate(S):
			if H:G.setdefault(H,[]).append((R,T))
	B=[]
	for(A,I)in G.items():J=[A for(A,B)in I];K=[A for(B,A)in I];B.append((A,min(J),max(J),min(K),max(K)))
	B.sort(key=lambda b:b[0]);U=sum(A[2]-A[1]+1 for A in B);L=0;M={}
	for(A,C,F,D,N)in reversed(B):M[A]=E-U+L;L+=F-C+1
	O=[[0]*E for A in range(E)]
	for(A,C,F,D,N)in B:
		V=F-C+1;W=N-D+1;X=M[A]
		for P in range(V):
			for Q in range(W):
				if g[C+P][D+Q]==A:O[X+P][D+Q]=A
	return O