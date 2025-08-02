def val_func_lrcorner(patch):return tuple(map(max,zip(*val_func_toindices(patch))))
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_ulcorner(patch):return tuple(map(min,zip(*val_func_toindices(patch))))
def val_func_vconcat(a,b):return a+b
def val_func_dmirror(piece):
	A=piece
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_hmirror(piece):
	A=piece
	if isinstance(A,tuple):return A[::-1]
	B=val_func_ulcorner(A)[0]+val_func_lrcorner(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def val_func_fork(outer,a,b):return lambda x:outer(a(x),b(x))
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_remove(value,container):A=container;return type(A)(A for A in A if A!=value)
def val_func_last(container):return max(enumerate(container))[1]
def val_func_dedupe(tup):return tuple(A for(B,A)in enumerate(tup)if tup.index(A)==B)
def val_func_identity(x):return x
def p(I):I=tuple(map(tuple,I));A=val_func_compose(val_func_dmirror,val_func_dedupe);C=A(I);D=A(C);E=val_func_fork(val_func_remove,val_func_last,val_func_identity);F=val_func_compose(val_func_hmirror,E);B=val_func_fork(val_func_vconcat,val_func_identity,F);G=B(D);H=val_func_dmirror(G);J=B(H);return[*map(list,J)]