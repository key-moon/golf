def p(I):
	J=False;F=None;A=True;u,v=len(I),len(I[0])
	def a(G):A=[B for A in G for B in A];return max(set(A),key=A.count)
	def b(G):return tuple(tuple(A)for A in zip(*G[::-1]))
	def c(G):return G[::-1]
	def d(G):return tuple(tuple(A[::-1])for A in G)
	def B(idx):A=[A for(A,B)in idx];B=[A for(B,A)in idx];return min(A),min(B),max(A),max(B)
	def K(idx):A,C,D,E=B(idx);return A+(D-A)//2,C+(E-C)//2
	def e(G,u,l,d,r):return tuple(tuple(G[A][l:r+1])for A in range(u,d+1))
	def P(G,obj):
		A=[list(A)for A in G]
		for(D,(B,C))in obj:
			if 0<=B<len(A)and 0<=C<len(A[0]):A[B][C]=D
		return tuple(tuple(A)for A in A)
	def Q(obj,di,dj):return{(A,(B+di,C+dj))for(A,(B,C))in obj}
	def D(G,univalued=A,ignore_bg=A):
		B=ignore_bg;C=a(G)if B else F;D,E=len(G),len(G[0])
		if univalued:
			J=sorted({G[A][D]for A in range(D)for D in range(E)if not B or G[A][D]!=C});I=[]
			for H in J:
				if B and H==C:continue
				A=[(A,B)for A in range(D)for B in range(E)if G[A][B]==H]
				if A:I.append({(H,(A,B))for(A,B)in A})
			return I
		else:
			A=[(A,D)for A in range(D)for D in range(E)if not B or G[A][D]!=C]
			if B:A=[(A,B)for(A,B)in A if G[A][B]!=C]
			if not A:return[]
			return[{(G[A][B],(A,B))for(A,B)in A}]
	def L(G,obj):F=[(A,B)for(C,(A,B))in obj];A,C,D,E=B(F);return e(G,A,C,D,E),(A,C,D,E)
	def R(obj,G):A,B=L(G,obj);return A==b(A)
	f=D(I,univalued=A,ignore_bg=A);g=sorted(f,key=lambda o:B([A for(B,A)in o]));G=F
	for C in g:
		if R(C,I):G=C;break
	if G is F:return I
	H=K([A for(B,A)in G]);S=D(I,univalued=J,ignore_bg=A)
	if not S:return I
	h=sorted(S,key=lambda o:B([A for(B,A)in o]))[0];i,j=L(I,h);M=c(i);T=D(M,univalued=J,ignore_bg=A)
	if not T:return I
	k=sorted(T,key=lambda o:B([A for(B,A)in o]))[0];l=D(M,univalued=A,ignore_bg=A);N=F
	for C in sorted(l,key=lambda o:B([A for(B,A)in o])):
		if R(C,M):N=C;break
	if N is F:return I
	U=K([A for(B,A)in N]);m,n=H[0]-U[0],H[1]-U[1];E=P(I,Q(k,m,n));V=D(E,univalued=J,ignore_bg=A)
	if not V:return E
	o=sorted(V,key=lambda o:B([A for(B,A)in o]))[0];p,j=L(E,o);W=d(p);X=D(W,univalued=J,ignore_bg=A)
	if not X:return E
	q=sorted(X,key=lambda o:B([A for(B,A)in o]))[0];Y=D(W,univalued=A,ignore_bg=A)
	if not Y:return E
	r=next(iter(G))[0];O=F
	for C in sorted(Y,key=lambda o:B([A for(B,A)in o])):
		if next(iter(C))[0]==r:O=C;break
	if O is F:return E
	Z=K([A for(B,A)in O]);s,t=H[0]-Z[0],H[1]-Z[1];return P(E,Q(q,s,t))
