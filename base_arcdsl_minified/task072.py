def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_bottomhalf(grid):A=grid;return A[len(A)//2+len(A)%2:]
def val_func_tophalf(grid):return grid[:len(grid)//2]
def val_func_canvas(value,dimensions):A=dimensions;return tuple(tuple(value for A in range(A[1]))for B in range(A[0]))
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def val_func_astuple(a,b):return a,b
def val_func_difference(a,b):return type(a)(A for A in a if A not in b)
def val_func_intersection(a,b):return a&b
def val_func_combine(a,b):return type(a)((*a,*b))
def p(I):I=tuple(map(tuple,I));C=val_func_tophalf(I);D=val_func_bottomhalf(I);E=val_func_astuple(6,5);A=val_func_ofcolor(C,2);B=val_func_ofcolor(D,2);F=val_func_combine(A,B);G=val_func_intersection(A,B);H=val_func_difference(F,G);J=val_func_canvas(0,E);K=val_func_fill(J,3,H);return[*map(list,K)]