def val_func_ival_func_neighbors(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(A):return val_func_dval_func_neighbors(A)|val_func_ival_func_neighbors(A)
def val_func_dval_func_neighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def val_func_mostval_func_color(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_dmirror(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_color(A):return next(iter(A))[0]
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_objects(A,B,C,D):
	K=val_func_mostval_func_color(A)if D else None;L=set();G=set();O,P=len(A),len(A[0]);Q=val_func_asindices(A);R=val_func_neighbors if C else val_func_dval_func_neighbors
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
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_chain(A,B,C):return lambda D:A(B(C(D)))
def val_func_branch(A,B,C):return B if A else C
def val_func_first(A):return next(iter(A))
def val_func_size(A):return len(A)
def val_func_repeat(A,B):return tuple(A for B in range(B))
def val_func_order(A,B):return tuple(sorted(A,key=B))
def val_func_dedupe(A):return tuple(B for(C,B)in enumerate(A)if A.index(B)==C)
def val_func_equality(A,B):return A==B
def val_func_identity(A):return A
def p(A):C=False;A=tuple(map(tuple,A));D=val_func_chain(val_func_size,val_func_dedupe,val_func_first);E=D(A);F=val_func_equality(E,1);B=val_func_branch(F,val_func_dmirror,val_func_identity);G=B(A);H=val_func_objects(G,True,C,C);I=val_func_order(H,val_func_leftmost);J=val_func_apply(val_func_color,I);K=val_func_repeat(J,1);L=B(K);return[*map(list,L)]