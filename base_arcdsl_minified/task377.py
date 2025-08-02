def val_func_lrcorner(A):return tuple(map(max,zip(*val_func_toindices(A))))
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_vconcat(A,B):return A+B
def val_func_dmirror(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_hmirror(A):
	if isinstance(A,tuple):return A[::-1]
	B=val_func_ulcorner(A)[0]+val_func_lrcorner(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def val_func_fork(A,B,C):return lambda D:A(B(D),C(D))
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_remove(A,B):return type(B)(B for B in B if B!=A)
def val_func_last(A):return max(enumerate(A))[1]
def val_func_dedupe(A):return tuple(B for(C,B)in enumerate(A)if A.index(B)==C)
def val_func_identity(A):return A
def p(A):A=tuple(map(tuple,A));B=val_func_compose(val_func_dmirror,val_func_dedupe);D=B(A);E=B(D);F=val_func_fork(val_func_remove,val_func_last,val_func_identity);G=val_func_compose(val_func_hmirror,F);C=val_func_fork(val_func_vconcat,val_func_identity,G);H=C(E);I=val_func_dmirror(H);J=C(I);return[*map(list,J)]