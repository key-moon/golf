def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_palette(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_lrcorner(A):return tuple(map(max,zip(*val_func_toindices(A))))
def val_func_vmirror(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=val_func_ulcorner(A)[1]+val_func_lrcorner(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def val_func_mostcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_hfrontier(A):return frozenset((A[0],B)for B in range(30))
def val_func_vfrontier(A):return frozenset((B,A[1])for B in range(30))
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
def val_func_underpaint(A,B):
	F,G=len(A),len(A[0]);H=val_func_mostcolor(A);C=list(list(A)for A in A)
	for(I,(D,E))in B:
		if 0<=D<F and 0<=E<G:
			if C[D][E]==H:C[D][E]=I
	return tuple(tuple(A)for A in C)
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_cmirror(A):
	if isinstance(A,tuple):return tuple(zip(*(A[::-1]for A in A[::-1])))
	return val_func_vmirror(val_func_dmirror(val_func_vmirror(A)))
def val_func_dmirror(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_fgpartition(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in val_func_palette(A)-{val_func_mostcolor(A)})
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def mval_func_apply(A,B):return val_func_merge(val_func_apply(A,B))
def val_func_fork(A,B,C):return lambda D:A(B(D),C(D))
def val_func_chain(A,B,C):return lambda D:A(B(C(D)))
def val_func_astuple(A,B):return A,B
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_difference(A,B):return type(A)(A for A in A if A not in B)
def val_func_combine(A,B):return type(A)((*A,*B))
def p(A):A=tuple(map(tuple,A));D=val_func_fgpartition(A);E=val_func_chain(val_func_cmirror,val_func_dmirror,val_func_merge);B=E(D);F=val_func_upscale(B,3);G=val_func_astuple(-2,-2);H=val_func_shift(F,G);I=val_func_underpaint(A,H);C=val_func_toindices(B);J=val_func_fork(val_func_combine,val_func_hfrontier,val_func_vfrontier);K=mval_func_apply(J,C);L=val_func_difference(K,C);M=val_func_fill(I,0,L);return[*map(list,M)]