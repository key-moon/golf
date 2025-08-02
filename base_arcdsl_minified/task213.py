def val_func_ival_func_neighbors(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(A):return val_func_dval_func_neighbors(A)|val_func_ival_func_neighbors(A)
def val_func_dval_func_neighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def val_func_mostval_func_color(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
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
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_replace(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def val_func_dmirror(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_color(A):return next(iter(A))[0]
def val_func_vline(A):return val_func_height(A)==len(A)and val_func_width(A)==1
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
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
def val_func_rbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(D,B)
	elif C==3:return lambda D,E:A(D,E,B)
	else:return lambda D,E,F:A(D,E,F,B)
def val_func_branch(A,B,C):return B if A else C
def val_func_first(A):return next(iter(A))
def val_func_size(A):return len(A)
def val_func_repeat(A,B):return tuple(A for B in range(B))
def val_func_order(A,B):return tuple(sorted(A,key=B))
def val_func_dedupe(A):return tuple(B for(C,B)in enumerate(A)if A.index(B)==C)
def val_func_identity(A):return A
def p(A):B=True;A=tuple(map(tuple,A));C=val_func_replace(A,5,0);F=val_func_objects(C,B,B,B);G=val_func_first(F);H=val_func_vline(G);D=val_func_branch(H,val_func_dmirror,val_func_identity);I=D(C);J=val_func_objects(I,B,B,B);K=val_func_order(J,val_func_uppermost);L=val_func_apply(val_func_color,K);E=val_func_dedupe(L);M=val_func_size(E);N=val_func_rbind(val_func_repeat,M);O=val_func_apply(N,E);P=D(O);return[*map(list,P)]