def p(z):
	B=tuple(tuple(A)for A in z);E,r=len(B),len(B[0]);i=[[False]*r for A in range(E)];I=[]
	def V(i,e):
		for(C,D)in((1,0),(-1,0),(0,1),(0,-1)):
			A,B=i+C,e+D
			if 0<=A<E and 0<=B<r:yield(A,B)
	for G in range(E):
		for D in range(r):
			b=B[G][D];J=[(G,D)];c=set()
			while J:
				A,C=J.pop();c.add((A,C))
				for(P,Q)in V(A,C):
					if not i[P][Q]and B[P][Q]==b:i[P][Q]=True;J.append((P,Q))
			I.append((b,c))
	x=[(B,A)for(B,A)in I if len(A)==1];R=[(B,A)for(B,A)in I if len(A)>1]
	if not R:return[list(A)for A in B]
	K={}
	for(A,p)in R:K[A]=K.get(A,0)+len(p)
	n=sorted(K.items(),key=lambda x:(-x[1],x[0]))
	if not n:return[list(A)for A in B]
	X=n[0][0];Y=n[1][0]if len(n)>1 else n[0][0];f={(A,C)for A in range(E)for C in range(r)if B[A][C]==X};J={(A,C)for A in range(E)for C in range(r)if B[A][C]==Y};I=[(1,1),(-1,-1),(1,-1),(-1,1)]
	def K(i,e,di,g):
		C=[];A,B=i,e
		while 0<=A<E and 0<=B<r:C.append((A,B));A+=di;B+=g
		return C
	H=[(A,B)for(A,B)in x if A not in(X,Y)]
	if not H:H=x[:]
	Z=set()
	for(i,p)in H:
		A,g=next(iter(p))
		for(D,V)in I:Z.update(K(A,g,D,V))
	R=Z&f;h=Z&J
	if H:
		C={}
		for(A,i)in H:C[A]=C.get(A,0)+1
		A=sorted(C.keys(),key=lambda r:(-C[r],r))
		if len(A)==1:A=A+[A[0]]
		M,N=A[0],A[1]
		def e(mc):
			C=D=0
			for(A,n)in H:
				if A!=mc:continue
				M,N=next(iter(n))
				for G in(-1,0,1):
					for I in(-1,0,1):
						if G==0 and I==0:continue
						A,J=M+G,N+I
						if 0<=A<E and 0<=J<r:
							K=B[A][J]
							if K==X:C+=1
							elif K==Y:D+=1
			return C-D
		a=e(M);S=e(N)
		if a>0 and S<0:T,U=M,N
		elif a<0 and S>0:T,U=N,M
		elif a==0 and S!=0:
			if S>0:T,U=N,M
			else:T,U=M,N
	else:return[list(A)for A in B]
	C=[list(A)for A in B]
	for(G,D)in R:C[G][D]=T
	for(G,D)in h:C[G][D]=U
	return C