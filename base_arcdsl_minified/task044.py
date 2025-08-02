def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_ival_func_neighbors(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(A):return val_func_dval_func_neighbors(A)|val_func_ival_func_neighbors(A)
def val_func_dval_func_neighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_mostcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_cover(A,B):return val_func_fill(A,val_func_mostcolor(A),val_func_toindices(B))
def val_func_paint(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_move(A,B,C):return val_func_paint(val_func_cover(A,B),val_func_shift(B,C))
def val_func_bordering(A,B):return val_func_uppermost(A)==0 or val_func_leftmost(A)==0 or val_func_lowermost(A)==len(B)-1 or val_func_rightmost(A)==len(B[0])-1
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
def val_func_normalize(A):
	if len(A)==0:return A
	return val_func_shift(A,(-val_func_uppermost(A),-val_func_leftmost(A)))
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_colorfilter(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def val_func_rbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(D,B)
	elif C==3:return lambda D,E:A(D,E,B)
	else:return lambda D,E,F:A(D,E,F,B)
def val_func_matcher(A,B):return lambda C:A(C)==B
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_last(A):return max(enumerate(A))[1]
def val_func_first(A):return next(iter(A))
def val_func_extract(A,B):return next(A for A in A if B(A))
def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_difference(A,B):return type(A)(A for A in A if A not in B)
def val_func_flip(A):return not A
def val_func_subtract(A,B):
	if isinstance(A,int)and isinstance(B,int):return A-B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]-B[0],A[1]-B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A-B[0],A-B[1]
	return A[0]-B,A[1]-B
def p(A):K=False;A=tuple(map(tuple,A));C=val_func_objects(A,True,K,K);D=val_func_colorfilter(C,0);L=val_func_rbind(val_func_bordering,A);M=val_func_compose(val_func_flip,L);E=val_func_sfilter(D,M);F=val_func_first(E);G=val_func_last(E);H=val_func_difference(C,D);B=val_func_compose(val_func_normalize,val_func_toindices);N=B(F);O=B(G);P=val_func_matcher(B,N);Q=val_func_matcher(B,O);I=val_func_extract(H,P);J=val_func_extract(H,Q);R=val_func_ulcorner(F);S=val_func_ulcorner(G);T=val_func_ulcorner(I);U=val_func_ulcorner(J);V=val_func_subtract(R,T);W=val_func_subtract(S,U);X=val_func_move(A,I,V);Y=val_func_move(X,J,W);return[*map(list,Y)]