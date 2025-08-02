def pval_func_apply(A,B,C):return tuple(A(B,C)for(B,C)in zip(B,C))
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_ival_func_neighbors(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(A):return val_func_dval_func_neighbors(A)|val_func_ival_func_neighbors(A)
def val_func_dval_func_neighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def val_func_mostval_func_color(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_paint(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def val_func_color(A):return next(iter(A))[0]
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
def reval_func_color(A,B):return frozenset((A,B)for B in val_func_toindices(B))
def mpval_func_apply(A,B,C):return val_func_merge(pval_func_apply(A,B,C))
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_size(A):return len(A)
def val_func_order(A,B):return tuple(sorted(A,key=B))
def val_func_invert(A):return-A if isinstance(A,int)else(-A[0],-A[1])
def p(A):C=False;A=tuple(map(tuple,A));B=val_func_objects(A,True,C,C);D=val_func_compose(val_func_invert,val_func_size);E=val_func_order(B,val_func_size);F=val_func_order(B,D);G=val_func_apply(val_func_color,F);H=mpval_func_apply(reval_func_color,G,E);I=val_func_paint(A,H);return[*map(list,I)]