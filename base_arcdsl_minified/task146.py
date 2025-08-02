def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_crop(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def val_func_vsplit(A,B):C,D=len(A)//B,len(A[0]);E=len(A)%B!=0;return tuple(val_func_crop(A,(C*B+B*E,0),(C,D))for B in range(B))
def val_func_dmirror(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_fork(A,B,C):return lambda D:A(B(D),C(D))
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_extract(A,B):return next(A for A in A if B(A))
def val_func_equality(A,B):return A==B
def val_func_flip(A):return not A
def val_func_identity(A):return A
def p(A):A=tuple(map(tuple,A));B=val_func_vsplit(A,3);C=val_func_fork(val_func_equality,val_func_dmirror,val_func_identity);D=val_func_compose(val_func_flip,C);E=val_func_extract(B,D);return[*map(list,E)]