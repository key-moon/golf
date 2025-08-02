def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
def ival_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_dval_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_palette(element):
	A=element
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
def val_func_normalize(patch):
	A=patch
	if len(A)==0:return A
	return val_func_shift(A,(-val_func_uppermost(A),-val_func_leftmost(A)))
def val_func_vperiod(obj):
	A=val_func_normalize(obj);C=val_func_height(A)
	for B in range(1,C):
		D=val_func_shift(A,(-B,0));E=frozenset({(B,(A,C))for(B,(A,C))in D if A>=0})
		if E.issubset(A):return B
def val_func_hperiod(obj):
	A=val_func_normalize(obj);B=val_func_width(A)
	for C in range(1,B):
		D=val_func_shift(A,(0,-C));E=frozenset({(B,(C,A))for(B,(C,A))in D if A>=0})
		if E.issubset(A):return C
	return B
def val_func_paint(grid,obj):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(G,(C,D))in obj:
		if 0<=C<E and 0<=D<F:B[C][D]=G
	return tuple(tuple(A)for A in B)
def val_func_asobject(grid):return frozenset((D,(A,C))for(A,B)in enumerate(grid)for(C,D)in enumerate(B))
def val_func_partition(grid):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(grid)for(E,A)in enumerate(D)if A==B)for B in val_func_palette(grid))
def val_func_neighbors(loc):return val_func_dval_func_neighbors(loc)|ival_func_neighbors(loc)
def val_func_shift(patch,directions):
	A=patch
	if len(A)==0:return A
	B,C=directions
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(D+B,E+C))for(A,(D,E))in A)
	return frozenset((A+B,D+C)for(A,D)in A)
def val_func_crop(grid,start,dims):A=start;return tuple(B[A[1]:A[1]+dims[1]]for B in grid[A[0]:A[0]+dims[0]])
def val_func_colorfilter(objs,value):return frozenset(A for A in objs if next(iter(A))[0]==value)
def val_func_width(piece):
	A=piece
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_height(piece):
	A=piece
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def mval_func_apply(function,container):return val_func_merge(val_func_apply(function,container))
def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_lbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def val_func_astuple(a,b):return a,b
def val_func_tojvec(j):return 0,j
def val_func_toivec(i):return i,0
def val_func_decrement(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_difference(a,b):return type(a)(A for A in a if A not in b)
def val_func_multiply(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def p(I):I=tuple(map(tuple,I));A=val_func_height(I);B=val_func_width(I);C=val_func_partition(I);D=val_func_colorfilter(C,0);E=val_func_difference(C,D);F=val_func_merge(E);G=val_func_astuple(A,1);H=val_func_astuple(1,B);J=val_func_decrement(A);K=val_func_decrement(B);L=val_func_toivec(K);M=val_func_tojvec(J);N=val_func_crop(I,L,H);O=val_func_crop(I,M,G);P=val_func_asobject(O);Q=val_func_asobject(N);R=val_func_vperiod(P);S=val_func_hperiod(Q);T=val_func_astuple(R,S);U=val_func_lbind(val_func_multiply,T);V=val_func_neighbors((0,0));W=mval_func_apply(val_func_neighbors,V);X=val_func_apply(U,W);Y=val_func_lbind(val_func_shift,F);Z=mval_func_apply(Y,X);a=val_func_paint(I,Z);return[*map(list,a)]