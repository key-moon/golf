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
def val_func_trim(grid):return tuple(A[1:-1]for A in grid[1:-1])
def val_func_connect(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def val_func_paint(grid,obj):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(G,(C,D))in obj:
		if 0<=C<E and 0<=D<F:B[C][D]=G
	return tuple(tuple(A)for A in B)
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_asobject(grid):return frozenset((D,(A,C))for(A,B)in enumerate(grid)for(C,D)in enumerate(B))
def val_func_shift(patch,directions):
	A=patch
	if len(A)==0:return A
	B,C=directions
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(D+B,E+C))for(A,(D,E))in A)
	return frozenset((A+B,D+C)for(A,D)in A)
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def mval_func_apply(function,container):return val_func_merge(val_func_apply(function,container))
def val_func_fork(outer,a,b):return lambda x:outer(a(x),b(x))
def val_func_power(function,n):
	A=function
	if n==1:return A
	return val_func_compose(A,val_func_power(A,n-1))
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_product(a,b):return frozenset((B,A)for A in b for B in a)
def val_func_last(container):return max(enumerate(container))[1]
def val_func_first(container):return next(iter(container))
def val_func_sfilter(container,condition):A=container;return type(A)(A for A in A if condition(A))
def val_func_intersection(a,b):return a&b
def val_func_equality(a,b):return a==b
def p(I):I=tuple(map(tuple,I));A=val_func_ofcolor(I,2);B=val_func_ofcolor(I,0);C=val_func_product(A,A);D=val_func_power(val_func_first,2);E=val_func_compose(val_func_first,val_func_last);F=val_func_fork(val_func_equality,D,E);G=val_func_sfilter(C,F);H=val_func_fork(val_func_connect,val_func_first,val_func_last);J=mval_func_apply(H,G);K=val_func_intersection(J,B);L=val_func_fill(I,9,K);M=val_func_trim(L);N=val_func_asobject(M);O=val_func_shift(N,(1,1));P=val_func_paint(I,O);return[*map(list,P)]