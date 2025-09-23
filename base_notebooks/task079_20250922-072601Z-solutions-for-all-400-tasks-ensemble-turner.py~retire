def p(g):
	A=[A[:]for A in g];G,H=len(A),len(A[0]);L=[B for A in A for B in A];Q=max(set(L),key=L.count);F=[[False]*H for A in range(G)];I=[]
	for B in range(G):
		for C in range(H):
			if A[B][C]==Q or F[B][C]:continue
			M=A[B][C];J=[(B,C)];N=[];F[B][C]=True
			while J:
				O,P=J.pop();N.append((O,P))
				for(R,S)in((1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)):
					D,E=O+R,P+S
					if 0<=D<G and 0<=E<H and not F[D][E]and A[D][E]==M:F[D][E]=True;J.append((D,E))
			I.append((M,N))
	from collections import Counter as T;K=T(A for(A,B)in I)
	if not K:return A
	U=max(K.keys(),key=lambda c:(K[c],c));V=[B for(A,B)in I if A==U]
	def W(cells):A=cells;B=[A for(A,B)in A];C=[A for(B,A)in A];return min(B),min(C),max(B),max(C)
	X,Y,Z,a=min((W(A),)for A in V)[0];return[A[Y:a+1]for A in A[X:Z+1]]
