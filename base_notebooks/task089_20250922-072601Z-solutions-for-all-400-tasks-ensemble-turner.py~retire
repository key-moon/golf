def p(g):
	D,E=len(g),len(g[0]);K=[A[:]for A in g];F=[[0]*E for A in range(D)];L=[]
	for G in range(D):
		for H in range(E):
			if F[G][H]or g[G][H]==0:continue
			I=[(G,H)];C=[]
			while I:
				A,B=I.pop()
				if A<0 or A>=D or B<0 or B>=E or F[A][B]or g[A][B]==0:continue
				F[A][B]=1;C.append((A,B,g[A][B]));I.extend([(A+C,B+G)for(C,G)in[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]if 0<=A+C<D and 0<=B+G<E and not F[A+C][B+G]and g[A+C][B+G]!=0])
			C and L.append(C)
	M,N,O,P=[],[],[],[]
	for C in L:
		Q={B for(A,A,B)in C}
		if len(C)==1:
			R,A,S=C[0]
			if S==2:O.append((R,A))
			elif S==3:P.append((R,A))
		else:
			if 2 in Q:M.append(C)
			if 3 in Q:N.append(C)
	def T(tp,tc,ms,f=0):
		B=next(((A,B)for(A,B,C)in tp if C==tc),None)
		if not B:return
		G,H=B
		for(I,J)in ms:
			for(L,M,N)in tp:
				O,A=L-G,M-H
				if f:A=-A
				C,F=I+O,J+A
				if 0<=C<D and 0<=F<E:K[C][F]=N
	for J in M:T(J,2,O,1)
	for J in N:T(J,3,P)
	return K