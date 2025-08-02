def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_crop(grid,start,dims):A=start;return tuple(B[A[1]:A[1]+dims[1]]for B in grid[A[0]:A[0]+dims[0]])
def val_func_hsplit(grid,n):A=grid;D,B=len(A),len(A[0])//n;E=len(A[0])%n!=0;return tuple(val_func_crop(A,(0,B*C+C*E),(D,B))for C in range(n))
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def val_func_remove(value,container):A=container;return type(A)(A for A in A if A!=value)
def val_func_last(container):return max(enumerate(container))[1]
def val_func_first(container):return next(iter(container))
def p(I):I=tuple(map(tuple,I));A=val_func_hsplit(I,3);B=val_func_first(A);C=val_func_remove(B,A);D=val_func_first(C);E=val_func_last(C);F=val_func_ofcolor(D,9);G=val_func_ofcolor(B,4);H=val_func_fill(E,9,F);J=val_func_fill(H,4,G);return[*map(list,J)]