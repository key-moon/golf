def p(g):
	if not g or not g[0]:return[A[:]for A in g]
	B=[A[:]for A in g];I,J=len(B),len(B[0]);from collections import Counter as Y
	def P(grid):A=Y(B for A in grid for B in A);return max(A,key=lambda k:A[k])
	def Z(i,j):
		for A in(-1,0,1):
			for B in(-1,0,1):
				if A==0 and B==0:continue
				C,D=i+A,j+B
				if 0<=C<I and 0<=D<J:yield(C,D)
	def C(grid):
		A=grid;N=P(A);J,K=len(A),len(A[0]);D,L=set(),[]
		for E in range(J):
			for F in range(K):
				if(E,F)in D:continue
				G=A[E][F]
				if G==N:continue
				H,I=set(),{(E,F)}
				while I:
					M=set()
					for(B,C)in I:
						if(B,C)in D:continue
						O=A[B][C]
						if O==G:H.add((B,C));D.add((B,C));[M.add((A,B))for(A,B)in Z(B,C)if 0<=A<J and 0<=B<K]
					I=M-D
				if H:L.append((G,tuple(sorted(H))))
		return L
	def D(pts):return min(A for(A,B)in pts)
	def K(pts):return min(A for(A,B)in pts),min(A for(B,A)in pts)
	def q(cp):B,A=cp;C,D=K(A);return B,tuple(sorted((A-C,B-D)for(A,B)in A))
	def Q(cp,dv):A,B=cp;C,D=dv;return A,tuple(sorted((A+C,B+D)for(A,B)in B))
	R=P(B);a=C(B);S={}
	for(L,A)in a:S[A]=L
	T=[(B,A)for(A,B)in S.items()]
	if not T:return[A[:]for A in B]
	E=sorted(T,key=lambda cp:(D(cp[1]),K(cp[1])[1]));M=D(E[0][1]);F=M
	for U in range(M+1,I):
		if any(B[U][A]!=R for A in range(J)):F=U
		elif F>=M:break
	G,N=set(),E[0][0]
	for(L,A)in E:
		if D(A)<=F:G.update(A)
		else:break
	b=min(A for(A,B)in G);c=min(A for(B,A)in G);d=tuple(sorted((A-b,B-c)for(A,B)in G));e=N,d
	def f(seq):
		E=None;G,A,B=[],E,-1
		for(J,C)in seq:
			H=D(C)
			if H<=F:continue
			I=max(A for(A,B)in C)
			if A is E or H>B+1:
				if A is not E:G.append((N,tuple(sorted(A))))
				A=set(C);B=I
			else:A.update(C);B=max(B,I)
		if A is not E:G.append((N,tuple(sorted(A))))
		return G
	h=f(E);i=[(0,2),(0,1),(0,0),(0,-1),(0,-2),(-1,0)];V=[]
	for(L,A)in h:j=K(A);k=Q(e,j);l=[set(Q(k,A)[1])for A in i];W=set(A);m=[(A,len(A&W),min(A for(A,B)in A)if A else float('inf'))for A in l];X=max(m,key=lambda x:(x[1],-x[2]));n=max(A for(B,A)in A);V.append((X[0]if X[1]>0 else W,n))
	C=[A[:]for A in B]
	for(o,p)in V:
		for(O,H)in o:
			if H<=p:continue
			if 0<=O<I and 0<=H<J and C[O][H]==R:C[O][H]=1
	return C
