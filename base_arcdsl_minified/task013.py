def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
def val_func_height(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def val_func_palette(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
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
def val_func_vfrontier(A):return frozenset((B,A[1])for B in range(30))
def val_func_paint(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def val_func_dmirror(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_color(A):return next(iter(A))[0]
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_fgpartition(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in val_func_palette(A)-{val_func_mostval_func_color(A)})
def reval_func_color(A,B):return frozenset((A,B)for B in val_func_toindices(B))
def val_func_portrait(A):return val_func_height(A)>val_func_width(A)
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def mval_func_apply(A,B):return val_func_merge(val_func_apply(A,B))
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
def val_func_branch(A,B,C):return B if A else C
def val_func_interval(A,B,C):return tuple(range(A,B,C))
def val_func_tojvec(A):return 0,A
def val_func_decrement(A):return A-1 if isinstance(A,int)else(A[0]-1,A[1]-1)
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_double(A):return A*2 if isinstance(A,int)else(A[0]*2,A[1]*2)
def val_func_identity(A):return A
def p(A):A=tuple(map(tuple,A));E=val_func_portrait(A);C=val_func_branch(E,val_func_dmirror,val_func_identity);B=C(A);D=val_func_fgpartition(B);F=val_func_merge(D);G=val_func_chain(val_func_double,val_func_decrement,val_func_width);H=G(F);I=val_func_compose(val_func_vfrontier,val_func_tojvec);J=val_func_lbind(mval_func_apply,I);K=val_func_rbind(val_func_interval,H);L=val_func_width(B);M=val_func_rbind(K,L);N=val_func_chain(J,M,val_func_leftmost);O=val_func_fork(reval_func_color,val_func_color,N);P=mval_func_apply(O,D);Q=val_func_paint(B,P);R=C(Q);return[*map(list,R)]