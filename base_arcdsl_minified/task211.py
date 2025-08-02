def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_lrcorner(A):return tuple(map(max,zip(*val_func_toindices(A))))
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_vconcat(A,B):return A+B
def val_func_hconcat(A,B):return tuple(A+B for(A,B)in zip(A,B))
def val_func_vmirror(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=val_func_ulcorner(A)[1]+val_func_lrcorner(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def val_func_hmirror(A):
	if isinstance(A,tuple):return A[::-1]
	B=val_func_ulcorner(A)[0]+val_func_lrcorner(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def p(A):A=tuple(map(tuple,A));C=val_func_vmirror(A);B=val_func_hconcat(C,A);D=val_func_hmirror(B);E=val_func_vconcat(B,D);F=val_func_vconcat(E,B);G=val_func_hmirror(F);return[*map(list,G)]