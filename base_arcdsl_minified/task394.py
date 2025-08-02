def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_ival_func_neighbors(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_dval_func_neighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def val_func_mostcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_shape(A):return val_func_height(A),val_func_width(A)
def val_func_crop(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
def val_func_normalize(A):
	if len(A)==0:return A
	return val_func_shift(A,(-val_func_uppermost(A),-val_func_leftmost(A)))
def val_func_height(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def val_func_vperiod(A):
	B=val_func_normalize(A);D=val_func_height(B)
	for C in range(1,D):
		E=val_func_shift(B,(-C,0));F=frozenset({(B,(A,C))for(B,(A,C))in E if A>=0})
		if F.issubset(B):return C
def val_func_hperiod(A):
	B=val_func_normalize(A);C=val_func_width(B)
	for D in range(1,C):
		E=val_func_shift(B,(0,-D));F=frozenset({(B,(C,A))for(B,(C,A))in E if A>=0})
		if F.issubset(B):return D
	return C
def val_func_vsplit(A,B):C,D=len(A)//B,len(A[0]);E=len(A)%B!=0;return tuple(val_func_crop(A,(C*B+B*E,0),(C,D))for B in range(B))
def val_func_hsplit(A,B):D,C=len(A),len(A[0])//B;E=len(A[0])%B!=0;return tuple(val_func_crop(A,(0,C*B+B*E),(D,C))for B in range(B))
def val_func_subgrid(A,B):return val_func_crop(B,val_func_ulcorner(A),val_func_shape(A))
def val_func_paint(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def val_func_asobject(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def val_func_palette(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_objects(A,B,C,D):
	K=val_func_mostcolor(A)if D else None;L=set();G=set();O,P=len(A),len(A[0]);Q=val_func_asindices(A);R=val_func_neighbors if C else val_func_dval_func_neighbors
	for E in Q:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==K:continue
		M={(H,E)};I={E}
		while len(I)>0:
			N=set()
			for F in I:
				J=A[F[0]][F[1]]
				if H==J if B else J!=K:M.add((J,F));G.add(F);N|={(A,B)for(A,B)in R(F)if 0<=A<O and 0<=B<P}
			I=N-G
		L.add(frozenset(M))
	return frozenset(L)
def val_func_neighbors(A):return val_func_dval_func_neighbors(A)|val_func_ival_func_neighbors(A)
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def mval_func_apply(A,B):return val_func_merge(val_func_apply(A,B))
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_lbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(B,D)
	elif C==3:return lambda D,E:A(B,D,E)
	else:return lambda D,E,F:A(B,D,E,F)
def val_func_rbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(D,B)
	elif C==3:return lambda D,E:A(D,E,B)
	else:return lambda D,E,F:A(D,E,F,B)
def val_func_chain(A,B,C):return lambda D:A(B(C(D)))
def val_func_astuple(A,B):return A,B
def val_func_extract(A,B):return next(A for A in A if B(A))
def val_func_mfilter(A,B):return val_func_merge(val_func_sfilter(A,B))
def val_func_contained(A,B):return A in B
def val_func_flip(A):return not A
def val_func_multiply(A,B):
	if isinstance(A,int)and isinstance(B,int):return A*B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]*B[0],A[1]*B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A*B[0],A*B[1]
	return A[0]*B,A[1]*B
def p(A):C=False;A=tuple(map(tuple,A));D=val_func_objects(A,True,C,C);E=val_func_ofcolor(A,0);F=val_func_lbind(val_func_contained,0);B=val_func_chain(val_func_flip,F,val_func_palette);G=val_func_mfilter(D,B);H=val_func_vsplit(A,2);I=val_func_hsplit(A,2);J=val_func_extract(H,B);K=val_func_extract(I,B);L=val_func_asobject(J);M=val_func_asobject(K);N=val_func_vperiod(L);O=val_func_hperiod(M);P=val_func_neighbors((0,0));Q=mval_func_apply(val_func_neighbors,P);R=val_func_astuple(N,O);S=val_func_rbind(val_func_multiply,R);T=val_func_apply(S,Q);U=val_func_lbind(val_func_shift,G);V=mval_func_apply(U,T);W=val_func_paint(A,V);X=val_func_subgrid(E,W);return[*map(list,X)]