def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_paint(grid,obj):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(G,(C,D))in obj:
		if 0<=C<E and 0<=D<F:B[C][D]=G
	return tuple(tuple(A)for A in B)
def val_func_asobject(grid):return frozenset((D,(A,C))for(A,B)in enumerate(grid)for(C,D)in enumerate(B))
def val_func_shift(patch,directions):
	A=patch
	if len(A)==0:return A
	B,C=directions
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(D+B,E+C))for(A,(D,E))in A)
	return frozenset((A+B,D+C)for(A,D)in A)
def val_func_crop(grid,start,dims):A=start;return tuple(B[A[1]:A[1]+dims[1]]for B in grid[A[0]:A[0]+dims[0]])
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def val_func_mval_func_apply(function,container):return val_func_merge(val_func_apply(function,container))
def val_func_lbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_decrement(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def p(I):I=tuple(map(tuple,I));A=val_func_ofcolor(I,1);B=val_func_crop(I,(0,0),(3,3));C=val_func_asobject(B);D=val_func_lbind(val_func_shift,C);E=val_func_compose(D,val_func_decrement);F=val_func_mval_func_apply(E,A);G=val_func_paint(I,F);return[*map(list,G)]