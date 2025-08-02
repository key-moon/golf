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
def val_func_hconcat(A,B):return tuple(A+B for(A,B)in zip(A,B))
def val_func_hmirror(A):
	if isinstance(A,tuple):return A[::-1]
	B=val_func_ulcorner(A)[0]+val_func_lrcorner(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def val_func_crop(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def val_func_astuple(A,B):return A,B
def p(A):A=tuple(map(tuple,A));D=val_func_astuple(2,1);C=val_func_crop(A,(0,0),D);E=val_func_hmirror(C);B=val_func_hconcat(C,E);F=val_func_hconcat(B,B);G=val_func_hconcat(F,B);return[*map(list,G)]