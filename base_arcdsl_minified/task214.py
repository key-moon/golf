def val_func_pval_func_apply(function,a,b):return tuple(function(A,B)for(A,B)in zip(a,b))
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_paint(grid,obj):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(G,(C,D))in obj:
		if 0<=C<E and 0<=D<F:B[C][D]=G
	return tuple(tuple(A)for A in B)
def val_func_rot180(grid):return tuple(tuple(A[::-1])for A in grid[::-1])
def val_func_rot90(grid):return tuple(A for A in zip(*grid[::-1]))
def val_func_asobject(grid):return frozenset((D,(A,C))for(A,B)in enumerate(grid)for(C,D)in enumerate(B))
def val_func_shift(patch,directions):
	A=patch
	if len(A)==0:return A
	B,C=directions
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(D+B,E+C))for(A,(D,E))in A)
	return frozenset((A+B,D+C)for(A,D)in A)
def val_func_crop(grid,start,dims):A=start;return tuple(B[A[1]:A[1]+dims[1]]for B in grid[A[0]:A[0]+dims[0]])
def mval_func_pval_func_apply(function,a,b):return val_func_merge(val_func_pval_func_apply(function,a,b))
def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_astuple(a,b):return a,b
def val_func_tojvec(j):return 0,j
def p(I):I=tuple(map(tuple,I));A=val_func_crop(I,(0,0),(3,3));B=val_func_rot90(A);C=val_func_rot180(A);D=val_func_astuple(B,C);E=val_func_astuple(4,8);F=val_func_apply(val_func_tojvec,E);G=val_func_apply(val_func_asobject,D);H=mval_func_pval_func_apply(val_func_shift,G,F);J=val_func_paint(I,H);return[*map(list,J)]