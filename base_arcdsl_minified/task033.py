def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_underfill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);G=val_func_mostval_func_color(A);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:
			if B[C][D]==G:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_asobject(grid):return frozenset((D,(A,C))for(A,B)in enumerate(grid)for(C,D)in enumerate(B))
def val_func_color(obj):return next(iter(obj))[0]
def val_func_palette(element):
	A=element
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_partition(grid):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(grid)for(E,A)in enumerate(D)if A==B)for B in val_func_palette(grid))
def val_func_shift(patch,directions):
	A=patch
	if len(A)==0:return A
	B,C=directions
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(D+B,E+C))for(A,(D,E))in A)
	return frozenset((A+B,D+C)for(A,D)in A)
def val_func_crop(grid,start,dims):A=start;return tuple(B[A[1]:A[1]+dims[1]]for B in grid[A[0]:A[0]+dims[0]])
def val_func_height(piece):
	A=piece
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def val_func_mostval_func_color(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_pval_func_apply(function,a,b):return tuple(function(A,B)for(A,B)in zip(a,b))
def mval_func_apply(function,container):return val_func_merge(val_func_apply(function,container))
def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_lbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def val_func_matcher(function,target):return lambda x:function(x)==target
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_product(a,b):return frozenset((B,A)for A in b for B in a)
def val_func_astuple(a,b):return a,b
def val_func_interval(start,stop,step):return tuple(range(start,stop,step))
def val_func_last(container):return max(enumerate(container))[1]
def val_func_first(container):return next(iter(container))
def val_func_totuple(container):return tuple(container)
def val_func_extract(container,condition):return next(A for A in container if condition(A))
def val_func_initset(value):return frozenset({value})
def val_func_difference(a,b):return type(a)(A for A in a if A not in b)
def val_func_flip(b):return not b
def val_func_divide(a,b):
	if isinstance(a,int)and isinstance(b,int):return a//b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]//b[0],a[1]//b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a//b[0],a//b[1]
	return a[0]//b,a[1]//b
def val_func_multiply(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def val_func_subtract(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def val_func_add(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):I=tuple(map(tuple,I));H=val_func_height(I);J=val_func_mostval_func_color(I);K=val_func_asobject(I);L=val_func_subtract(H,2);A=val_func_divide(L,3);M=val_func_astuple(A,A);N=val_func_crop(I,(0,0),M);O=val_func_partition(N);P=val_func_matcher(val_func_color,0);Q=val_func_compose(val_func_flip,P);B=val_func_extract(O,Q);R=val_func_initset(J);S=val_func_palette(K);T=val_func_palette(B);U=val_func_difference(S,T);V=val_func_difference(U,R);W=val_func_first(V);C=val_func_interval(0,3,1);X=val_func_product(C,C);D=val_func_totuple(X);E=val_func_apply(val_func_first,D);F=val_func_apply(val_func_last,D);G=val_func_lbind(val_func_multiply,A);Y=val_func_apply(G,E);Z=val_func_apply(G,F);a=val_func_pval_func_apply(val_func_add,Y,E);b=val_func_pval_func_apply(val_func_add,Z,F);c=val_func_pval_func_apply(val_func_astuple,a,b);d=val_func_lbind(val_func_shift,B);e=mval_func_apply(d,c);f=val_func_underfill(I,W,e);return[*map(list,f)]