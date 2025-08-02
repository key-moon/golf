def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_tophalf(grid):return grid[:len(grid)//2]
def val_func_bottomhalf(grid):A=grid;return A[len(A)//2+len(A)%2:]
def val_func_rot270(grid):return tuple(tuple(A[::-1])for A in zip(*grid[::-1]))[::-1]
def val_func_rot90(grid):return tuple(A for A in zip(*grid[::-1]))
def val_func_righthalf(grid):return val_func_rot270(val_func_bottomhalf(val_func_rot90(grid)))
def val_func_lefthalf(grid):return val_func_rot270(val_func_tophalf(val_func_rot90(grid)))
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def val_func_combine(a,b):return type(a)((*a,*b))
def p(I):I=tuple(map(tuple,I));A=val_func_lefthalf(I);B=val_func_righthalf(I);C=val_func_ofcolor(A,4);D=val_func_ofcolor(B,3);E=val_func_combine(C,D);F=val_func_fill(A,6,E);return[*map(list,F)]