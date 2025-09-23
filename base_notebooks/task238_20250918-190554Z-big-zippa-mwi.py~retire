def _most_color(grid):
	B=grid
	if not B or not B[0]:return 0
	A={}
	for D in B:
		for C in D:A[C]=A.get(C,0)+1
	return max(A,key=A.get)
def objects(grid,univalued,diagonal,without_bg):
	L=univalued;A=grid
	if not A or not A[0]:return[]
	M,N=len(A),len(A[0]);O=_most_color(A)if without_bg else None;P=[(-1,0),(1,0),(0,-1),(0,1)]
	if diagonal:P+=[(-1,-1),(-1,1),(1,-1),(1,1)]
	D,Q=set(),[]
	for E in range(M):
		for F in range(N):
			if(E,F)in D:continue
			R=A[E][F]
			if R==O:continue
			G,H=set(),[(E,F)]
			while H:
				B,C=H.pop()
				if(B,C)in D:continue
				I=A[B][C]
				if L and I!=R or not L and I==O:continue
				D.add((B,C));G.add((I,(B,C)))
				for(S,T)in P:
					J,K=B+S,C+T
					if 0<=J<M and 0<=K<N and(J,K)not in D:H.append((J,K))
			if G:Q.append(G)
	return Q
def _toindices(obj):
	A=obj
	if not A:return set()
	B=next(iter(A))
	if isinstance(B,tuple)and len(B)==2 and isinstance(B[1],tuple):return{(A,B)for(C,(A,B))in A}
	return set(A)
def _bbox_corners(patch):A=_toindices(patch);B=min(A for(A,B)in A);C=min(A for(B,A)in A);D=max(A for(A,B)in A);E=max(A for(B,A)in A);return(B,C),(D,E)
def _normalize(obj):
	A=obj
	if not A:return A
	(B,C),D=_bbox_corners(A);return{(A,(D-B,E-C))for(A,(D,E))in A}
def _shift(patch,d):
	A=patch;C,D=d
	if not A:return A
	B=next(iter(A))
	if isinstance(B,tuple)and len(B)==2 and isinstance(B[1],tuple):return{(A,(B+C,E+D))for(A,(B,E))in A}
	return{(A+C,B+D)for(A,B)in A}
def _crop(grid,start,dims):A,B=start;C,D=dims;return[A[B:B+D]for A in grid[A:A+C]]
def _subgrid(patch,grid):(A,B),(C,D)=_bbox_corners(patch);return _crop(grid,(A,B),(C-A+1,D-B+1))
def _vmirror(idx):
	A=_toindices(idx)
	if not A:return set()
	(B,C),(B,D)=_bbox_corners(A);E=C+D;return{(A,E-B)for(A,B)in A}
def _connect(a,b):
	A,B=a;C,D=b;E,F=min(A,C),min(B,D);G,H=max(A,C),max(B,D)
	if A==C:return{(A,B)for B in range(F,H+1)}
	if B==D:return{(A,B)for A in range(E,G+1)}
	if C-A==D-B:return{(A,B)for(A,B)in zip(range(E,G+1),range(F,H+1))}
	if C-A==B-D:return{(A,B)for(A,B)in zip(range(E,G+1),range(H,F-1,-1))}
	return set()
def _paint(grid,obj):
	A=grid;B=len(A);F=len(A[0])if B and A[0]else 0;C=[list(A)for A in A]
	for(G,(D,E))in obj:
		if 0<=D<B and 0<=E<F:C[D][E]=G
	return C
def _fill(grid,value,idx):
	A=grid;B=len(A);F=len(A[0])if B and A[0]else 0;C=[list(A)for A in A]
	for(D,E)in _toindices(idx):
		if 0<=D<B and 0<=E<F:C[D][E]=value
	return C
def _numcolors(obj):return len({A for(A,B)in obj})
def solve_9aec4887(I):
	A=objects(I,univalued=False,diagonal=True,without_bg=True)
	if not A:return I
	G={(8,(A,C))for(A,B)in enumerate(I)for(C,D)in enumerate(B)if D==8};H=lambda o:len(_toindices(o));J=G or min(A,key=_numcolors);K=[A for A in A if{A for(A,B)in A}!={8}]or A;B=max(K,key=H,default=None)
	if not B:return I
	D={(A,B)for(A,B)in B if A!=8};L=_subgrid(D or B,I);C=_toindices(_shift(_normalize(J),(1,1)));E=list(_normalize(D or B));M=_paint(L,[(min(E,key=lambda t,i=A,j=B:abs(t[1][0]-i)+abs(t[1][1]-j))[0]if E else 0,(A,B))for(A,B)in C]);(N,O),(P,Q)=_bbox_corners(C);F=_connect((N,O),(P,Q));R=C&(F|_vmirror(F));return _fill(M,8,R)
def p(g):return solve_9aec4887(g)