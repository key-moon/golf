def val_func_ival_func_neighbors(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(A):return val_func_dval_func_neighbors(A)|val_func_ival_func_neighbors(A)
def val_func_dval_func_neighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def val_func_lrcorner(A):return tuple(map(max,zip(*val_func_toindices(A))))
def val_func_llcorner(A):return tuple(map(lambda B:{0:max,1:min}[B[0]](B[1]),enumerate(zip(*val_func_toindices(A)))))
def val_func_urcorner(A):return tuple(map(lambda B:{0:min,1:max}[B[0]](B[1]),enumerate(zip(*val_func_toindices(A)))))
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_mostval_func_color(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
def val_func_outbox(A):F,G=val_func_uppermost(A)-1,val_func_leftmost(A)-1;H,I=val_func_lowermost(A)+1,val_func_rightmost(A)+1;B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def val_func_cover(A,B):return val_func_fill(A,val_func_mostval_func_color(A),val_func_toindices(B))
def val_func_corners(A):return frozenset({val_func_ulcorner(A),val_func_urcorner(A),val_func_llcorner(A),val_func_lrcorner(A)})
def val_func_paint(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def val_func_color(A):return next(iter(A))[0]
def val_func_manhattan(A,B):return min(abs(A-D)+abs(C-E)for(A,C)in val_func_toindices(A)for(D,E)in val_func_toindices(B))
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
def val_func_val_func_sizefilter(A,B):return frozenset(A for A in A if len(A)==B)
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_fork(A,B,C):return lambda D:A(B(D),C(D))
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
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_astuple(A,B):return A,B
def val_func_initset(A):return frozenset({A})
def val_func_argmax(A,B):return max(A,key=B)
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_size(A):return len(A)
def val_func_identity(A):return A
def p(A):A=tuple(map(tuple,A));B=val_func_objects(A,True,False,True);C=val_func_val_func_sizefilter(B,1);D=val_func_argmax(B,val_func_size);E=val_func_outbox(D);F=val_func_corners(E);G=val_func_lbind(val_func_rbind,val_func_manhattan);H=val_func_lbind(val_func_argmax,C);I=val_func_chain(H,G,val_func_initset);J=val_func_compose(val_func_color,I);K=val_func_fork(val_func_astuple,J,val_func_identity);L=val_func_apply(K,F);M=val_func_merge(C);N=val_func_cover(A,M);O=val_func_paint(N,L);return[*map(list,O)]