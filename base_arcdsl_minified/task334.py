def val_func_remove(value,container):A=container;return type(A)(A for A in A if A!=value)
def val_func_first(container):return next(iter(container))
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_hfrontier(location):return frozenset((location[0],A)for A in range(30))
def val_func_vfrontier(location):return frozenset((A,location[1])for A in range(30))
def val_func_canvas(value,dimensions):A=dimensions;return tuple(tuple(value for A in range(A[1]))for B in range(A[0]))
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_palette(element):
	A=element
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_fork(outer,a,b):return lambda x:outer(a(x),b(x))
def val_func_branch(condition,a,b):return a if condition else b
def val_func_other(container,value):return val_func_first(val_func_remove(value,container))
def val_func_combine(a,b):return type(a)((*a,*b))
def val_func_equality(a,b):return a==b
def p(I):I=tuple(map(tuple,I));B=val_func_palette(I);A=val_func_other(B,0);C=val_func_equality(A,1);D=val_func_equality(A,2);E=val_func_branch(C,(1,1),(2,2));F=val_func_branch(D,(0,1),E);G=val_func_fork(val_func_combine,val_func_vfrontier,val_func_hfrontier);H=G(F);J=val_func_canvas(0,(3,3));K=val_func_fill(J,5,H);return[*map(list,K)]