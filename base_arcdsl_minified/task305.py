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
def val_func_ulcorner(patch):return tuple(map(min,zip(*val_func_toindices(patch))))
def val_func_paint(grid,obj):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(G,(C,D))in obj:
		if 0<=C<E and 0<=D<F:B[C][D]=G
	return tuple(tuple(A)for A in B)
def val_func_dmirror(piece):
	A=piece
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_toobject(patch,grid):A=grid;D,E=len(A),len(A[0]);return frozenset((A[B][C],(B,C))for(B,C)in val_func_toindices(patch)if 0<=B<D and 0<=C<E)
def val_func_shift(patch,directions):
	A=patch
	if len(A)==0:return A
	B,C=directions
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(D+B,E+C))for(A,(D,E))in A)
	return frozenset((A+B,D+C)for(A,D)in A)
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
def val_func_pval_func_apply(function,a,b):return tuple(function(A,B)for(A,B)in zip(a,b))
def mval_func_apply(function,container):return val_func_merge(val_func_apply(function,container))
def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_lbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def val_func_pair(a,b):return tuple(zip(a,b))
def val_func_interval(start,stop,step):return tuple(range(start,stop,step))
def val_func_maximum(container):return max(container,default=0)
def val_func_difference(a,b):return type(a)(A for A in a if A not in b)
def val_func_invert(n):return-n if isinstance(n,int)else(-n[0],-n[1])
def p(I):I=tuple(map(tuple,I));C=val_func_asindices(I);D=val_func_dmirror(I);B=val_func_invert(9);E=val_func_pval_func_apply(val_func_pair,I,D);F=val_func_lbind(val_func_apply,val_func_maximum);A=val_func_apply(F,E);G=val_func_ofcolor(A,0);H=val_func_difference(C,G);J=val_func_toobject(H,A);K=val_func_interval(B,9,1);L=val_func_interval(9,B,-1);M=val_func_pair(K,L);N=val_func_lbind(val_func_shift,J);O=mval_func_apply(N,M);P=val_func_paint(A,O);return[*map(list,P)]