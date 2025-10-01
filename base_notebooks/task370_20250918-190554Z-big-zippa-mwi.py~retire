def solve_e8dc4411(I):
	if not I or not I[0]:return I
	D,E=len(I),len(I[0]);X=[B for A in I for B in A];Y=min(set(X),key=X.count);C={(A,B)for A in range(D)for B in range(E)if I[A][B]==0}
	if not C:return I
	R={(A,B)for A in range(D)for B in range(E)if I[A][B]==Y}
	def Z(idx):A=[A for(A,B)in idx];B=[A for(B,A)in idx];return min(A),min(B),max(A),max(B)
	def a(idx):A,B,C,D=Z(idx);return(A+C)//2,(B+D)//2
	def g(a,b):
		A,B=a;C,D=b;E=[]
		if A==C:
			F,G=sorted((B,D))
			for H in range(F,G+1):E.append((A,H))
		elif B==D:
			I,J=sorted((A,C))
			for K in range(I,J+1):E.append((K,B))
		elif C-A==D-B:
			I,J=sorted((A,C));F,G=sorted((B,D))
			for(K,H)in zip(range(I,J+1),range(F,G+1)):E.append((K,H))
		elif C-A==-(D-B):
			I,J=sorted((A,C));F,G=sorted((B,D))
			for(K,H)in zip(range(I,J+1),range(G,F-1,-1)):E.append((K,H))
		return E
	S,T,U,V=Z(C);h=set(g((S,T),(U,V))).issubset(C)
	def M(x):return(x>0)-(x<0)
	i,j=a(C);k,l=a(R);b,W=M(k-i),M(l-j);N,O=U-S+1,V-T+1;G=N*b,O*W;c=len(C)==2*(N+O)-4
	if c:J=G
	else:J=G if h else(G[0]-M(G[0]),G[1]-M(G[1]))
	F=set()
	if c:
		for H in range(1,5):
			A,B=H*J[0],H*J[1];d,m,e,n=S+A,T+B,U+A,V+B;K=0<=d and e<D;L=0<=m and n<E
			if K and L:F.update({(C+A,D+B)for(C,D)in C});continue
			if H==1:F.update({(C+A,F+B)for(C,F)in C if 0<=C+A<D and 0<=F+B<E});break
			if not K and L:F.update({(C+A,E+B)for(C,E)in C if 0<=C+A<D})
			elif not K and not L:F.update({(C+A,F+B)for(C,F)in C if 0<=C+A<D and 0<=F+B<E})
			elif K and not L and(W<0 or N==3 and O==3):F.update({(D+A,C+B)for(D,C)in C if 0<=C+B<E})
			elif K and not L and(e>=D-1 or d<=0):F.update({(C+A,F+B)for(C,F)in C if 0<=C+A<D and 0<=F+B<E})
			break
	else:
		for H in range(1,5):A,B=H*J[0],H*J[1];F.update({(C+A,F+B)for(C,F)in C if 0<=C+A<D and 0<=F+B<E})
	if len(C)==8 and N==3 and O==3 and len(R)==1:o,p=next(iter(R));P,Q=o+b,p+W;q={(P-1,Q+A)for A in(-1,0,1)}|{(P,Q-1),(P,Q+1)}|{(P+1,Q+A)for A in(-1,0,1)};F|={(A,B)for(A,B)in q if 0<=A<D and 0<=B<E}
	f=[list(A)for A in I]
	for(r,s)in F:f[r][s]=Y
	return tuple(map(tuple,f))
def p(g):return[list(A)for A in solve_e8dc4411(tuple(map(tuple,g)))]