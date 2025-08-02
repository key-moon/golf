def val_func_pval_func_apply(function,a,b):return tuple(function(A,B)for(A,B)in zip(a,b))
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_palette(element):
	A=element
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_paint(grid,obj):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(G,(C,D))in obj:
		if 0<=C<E and 0<=D<F:B[C][D]=G
	return tuple(tuple(A)for A in B)
def val_func_color(obj):return next(iter(obj))[0]
def val_func_partition(grid):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(grid)for(E,A)in enumerate(D)if A==B)for B in val_func_palette(grid))
def val_func_reval_func_color(value,patch):return frozenset((value,A)for A in val_func_toindices(patch))
def mval_func_pval_func_apply(function,a,b):return val_func_merge(val_func_pval_func_apply(function,a,b))
def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_remove(value,container):A=container;return type(A)(A for A in A if A!=value)
def val_func_last(container):return max(enumerate(container))[1]
def val_func_size(container):return len(container)
def val_func_repeat(item,num):return tuple(item for A in range(num))
def val_func_order(container,compfunc):return tuple(sorted(container,key=compfunc))
def val_func_combine(a,b):return type(a)((*a,*b))
def p(I):I=tuple(map(tuple,I));C=val_func_partition(I);A=val_func_order(C,val_func_size);D=val_func_apply(val_func_color,A);B=val_func_last(A);E=val_func_remove(B,A);F=val_func_repeat(B,1);G=val_func_combine(F,E);H=mval_func_pval_func_apply(val_func_reval_func_color,D,G);J=val_func_paint(I,H);return[*map(list,J)]