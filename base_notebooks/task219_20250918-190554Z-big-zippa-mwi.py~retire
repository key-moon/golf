def p(g):
	if not g or not g[0]:return[A[:]for A in g]
	B=[A[:]for A in g];H,I=len(B),len(B[0]);from collections import Counter as Z
	def Q(grid):A=Z(B for A in grid for B in A);return max(A,key=lambda k:A[k])
	def a(i,j):
		for A in(-1,0,1):
			for B in(-1,0,1):
				if A==0 and B==0:continue
				C,D=i+A,j+B
				if 0<=C<H and 0<=D<I:yield(C,D)
	def b(grid):
		A=grid;P=Q(A);J,K=len(A),len(A[0]);D=set();L=[]
		for E in range(J):
			for F in range(K):
				if(E,F)in D:continue
				G=A[E][F]
				if G==P:continue
				H=set();I={(E,F)}
				while I:
					M=set()
					for(B,C)in I:
						if(B,C)in D:continue
						R=A[B][C]
						if R==G:
							H.add((B,C));D.add((B,C))
							for(N,O)in a(B,C):
								if 0<=N<J and 0<=O<K:M.add((N,O))
					I=M-D
				if H:L.append((G,tuple(sorted(H))))
		return L
	def C(points):return min(A for(A,B)in points)
	def J(points):A=points;return min(A for(A,B)in A),min(A for(B,A)in A)
	def r(col_points):B,A=col_points;C,D=J(A);return B,tuple(sorted((A-C,B-D)for(A,B)in A))
	def R(col_points,dv):A,B=col_points;C,D=dv;return A,tuple(sorted((A+C,B+D)for(A,B)in B))
	S=Q(B);c=b(B);T={}
	for(K,A)in c:T[A]=K
	U=[(B,A)for(A,B)in T.items()]
	if not U:return[A[:]for A in B]
	D=sorted(U,key=lambda cp:(C(cp[1]),J(cp[1])[1]));L=C(D[0][1]);E=L
	for V in range(L+1,H):
		if any(B[V][A]!=S for A in range(I)):E=V
		elif E>=L:break
	F=set();M=D[0][0]
	for(K,A)in D:
		if C(A)<=E:F.update(A)
		else:break
	d=min(A for(A,B)in F);e=min(A for(B,A)in F);f=tuple(sorted((A-d,B-e)for(A,B)in F));h=M,f
	def i(seq):
		F=None;G=[];A=F;B=-1
		for(J,D)in seq:
			I=C(D)
			if I<=E:continue
			H=max(A for(A,B)in D)
			if A is F or I>B+1:
				if A is not F:G.append((M,tuple(sorted(A))))
				A=set(D);B=H
			else:
				A.update(D)
				if H>B:B=H
		if A is not F:G.append((M,tuple(sorted(A))))
		return G
	j=i(D);k=[(0,2),(0,1),(0,0),(0,-1),(0,-2),(-1,0)];N=[]
	for(K,A)in j:
		l=J(A);m=R(h,l);n=[set(R(m,A)[1])for A in k];W=set(A);o=[(A,len(A&W),min(A for(A,B)in A)if A else float('inf'))for A in n];X=max(o,key=lambda x:(x[1],-x[2]));Y=max(A for(B,A)in A)
		if X[1]>0:N.append((X[0],Y))
		else:N.append((W,Y))
	O=[A[:]for A in B]
	for(p,q)in N:
		for(P,G)in p:
			if G<=q:continue
			if 0<=P<H and 0<=G<I and O[P][G]==S:O[P][G]=1
	return O