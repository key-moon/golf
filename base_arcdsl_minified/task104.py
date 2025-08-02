def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_height(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_ival_func_neighbors(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(A):return val_func_dval_func_neighbors(A)|val_func_ival_func_neighbors(A)
def val_func_dval_func_neighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def val_func_mostcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_canvas(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def val_func_upscale(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for I in A:
			D=tuple()
			for E in I:D=D+tuple(E for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		F,G=val_func_ulcorner(A);J,K=-F,-G;L=val_func_shift(A,(J,K));H=set()
		for(E,(M,N))in L:
			for O in range(B):
				for P in range(B):H.add((E,(M*B+O,N*B+P)))
		return val_func_shift(frozenset(H),(F,G))
def val_func_paint(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def val_func_rot270(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def val_func_rot180(A):return tuple(tuple(A[::-1])for A in A[::-1])
def val_func_rot90(A):return tuple(A for A in zip(*A[::-1]))
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
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_shape(A):return val_func_height(A),val_func_width(A)
def val_func_branch(A,B,C):return B if A else C
def val_func_astuple(A,B):return A,B
def val_func_first(A):return next(iter(A))
def val_func_initset(A):return frozenset({A})
def val_func_combine(A,B):return type(A)((*A,*B))
def val_func_contained(A,B):return A in B
def p(A):E=False;A=tuple(map(tuple,A));F=val_func_objects(A,E,E,True);G=val_func_first(F);C=val_func_toindices(G);H=val_func_contained((0,2),C);I=val_func_contained((2,2),C);J=val_func_contained((2,0),C);K=val_func_astuple(9,9);L=val_func_canvas(0,K);M=val_func_astuple(3,(0,0));N=val_func_initset(M);O=val_func_upscale(N,2);D=val_func_upscale(O,2);P=val_func_shape(D);Q=val_func_shift(D,P);R=val_func_combine(D,Q);B=val_func_paint(L,R);S=val_func_rot90(B);T=val_func_rot180(B);U=val_func_rot270(B);V=val_func_branch(H,S,B);W=val_func_branch(I,T,V);X=val_func_branch(J,U,W);return[*map(list,X)]