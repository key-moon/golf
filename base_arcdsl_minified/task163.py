def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
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
def val_func_replace(grid,val_func_replacee,val_func_replacer):return tuple(tuple(val_func_replacer if A==val_func_replacee else A for A in A)for A in grid)
def val_func_paint(grid,obj):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(G,(C,D))in obj:
		if 0<=C<E and 0<=D<F:B[C][D]=G
	return tuple(tuple(A)for A in B)
def val_func_toobject(patch,grid):A=grid;D,E=len(A),len(A[0]);return frozenset((A[B][C],(B,C))for(B,C)in val_func_toindices(patch)if 0<=B<D and 0<=C<E)
def val_func_shift(patch,directions):
	A=patch
	if len(A)==0:return A
	B,C=directions
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(D+B,E+C))for(A,(D,E))in A)
	return frozenset((A+B,D+C)for(A,D)in A)
def val_func_recolor(value,patch):return frozenset((value,A)for A in val_func_toindices(patch))
def val_func_crop(grid,start,dims):A=start;return tuple(B[A[1]:A[1]+dims[1]]for B in grid[A[0]:A[0]+dims[0]])
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
def mval_func_apply(function,container):return val_func_merge(val_func_apply(function,container))
def val_func_lbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def val_func_branch(condition,a,b):return a if condition else b
def val_func_product(a,b):return frozenset((B,A)for A in b for B in a)
def val_func_astuple(a,b):return a,b
def val_func_insert(value,container):return container.union(frozenset({value}))
def val_func_last(container):return max(enumerate(container))[1]
def val_func_first(container):return next(iter(container))
def val_func_initset(value):return frozenset({value})
def val_func_greater(a,b):return a>b
def val_func_multiply(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def p(I):I=tuple(map(tuple,I));F=val_func_ofcolor(I,4);B=val_func_first(F);C=val_func_first(B);D=val_func_last(B);G=val_func_greater(C,3);H=val_func_greater(C,7);J=val_func_greater(D,3);K=val_func_greater(D,7);L=val_func_branch(G,4,0);M=val_func_branch(H,8,L);N=val_func_branch(J,4,0);O=val_func_branch(K,8,N);P=val_func_astuple(M,O);Q=val_func_initset(0);R=val_func_insert(4,Q);E=val_func_insert(8,R);S=val_func_product(E,E);T=val_func_crop(I,(0,0),(3,3));U=val_func_asindices(T);V=val_func_recolor(0,U);W=val_func_lbind(val_func_shift,V);X=mval_func_apply(W,S);Y=val_func_paint(I,X);Z=val_func_crop(I,P,(3,3));A=val_func_replace(Z,5,0);a=val_func_ofcolor(A,4);b=val_func_first(a);c=val_func_asindices(A);d=val_func_toobject(c,A);e=val_func_multiply(b,4);f=val_func_shift(d,e);g=val_func_paint(Y,f);return[*map(list,g)]