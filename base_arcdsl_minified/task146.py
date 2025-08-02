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
def val_func_crop(grid,start,dims):A=start;return tuple(B[A[1]:A[1]+dims[1]]for B in grid[A[0]:A[0]+dims[0]])
def val_func_vsplit(grid,n):A=grid;B,D=len(A)//n,len(A[0]);E=len(A)%n!=0;return tuple(val_func_crop(A,(B*C+C*E,0),(B,D))for C in range(n))
def val_func_dmirror(piece):
	A=piece
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_fork(outer,a,b):return lambda x:outer(a(x),b(x))
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_extract(container,condition):return next(A for A in container if condition(A))
def val_func_equality(a,b):return a==b
def val_func_flip(b):return not b
def val_func_identity(x):return x
def p(I):I=tuple(map(tuple,I));A=val_func_vsplit(I,3);B=val_func_fork(val_func_equality,val_func_dmirror,val_func_identity);C=val_func_compose(val_func_flip,B);D=val_func_extract(A,C);return[*map(list,D)]