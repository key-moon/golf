def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def ival_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(loc):return val_func_dval_func_neighbors(loc)|ival_func_neighbors(loc)
def val_func_dval_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_mostcolor(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
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
def val_func_crop(grid,start,dims):A=start;return tuple(B[A[1]:A[1]+dims[1]]for B in grid[A[0]:A[0]+dims[0]])
def val_func_shape(piece):A=piece;return val_func_height(A),val_func_width(A)
def val_func_hfrontier(location):return frozenset((location[0],A)for A in range(30))
def val_func_vfrontier(location):return frozenset((A,location[1])for A in range(30))
def val_func_trim(grid):return tuple(A[1:-1]for A in grid[1:-1])
def val_func_subgrid(patch,grid):A=patch;return val_func_crop(grid,val_func_ulcorner(A),val_func_shape(A))
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_palette(element):
	A=element
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
def val_func_objects(grid,univalued,diagonal,without_bg):
	A=grid;H=val_func_mostcolor(A)if without_bg else None;I=set();D=set();L,M=len(A),len(A[0]);N=val_func_asindices(A);O=val_func_neighbors if diagonal else val_func_dval_func_neighbors
	for B in N:
		if B in D:continue
		E=A[B[0]][B[1]]
		if E==H:continue
		J={(E,B)};F={B}
		while len(F)>0:
			K=set()
			for C in F:
				G=A[C[0]][C[1]]
				if E==G if univalued else G!=H:J.add((G,C));D.add(C);K|={(A,B)for(A,B)in O(C)if 0<=A<L and 0<=B<M}
			F=K-D
		I.add(frozenset(J))
	return frozenset(I)
def val_func_shift(patch,directions):
	A=patch
	if len(A)==0:return A
	B,C=directions
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(D+B,E+C))for(A,(D,E))in A)
	return frozenset((A+B,D+C)for(A,D)in A)
def val_func_ulcorner(patch):return tuple(map(min,zip(*val_func_toindices(patch))))
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
def val_func_leastcolor(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def mval_func_apply(function,container):return val_func_merge(val_func_apply(function,container))
def val_func_fork(outer,a,b):return lambda x:outer(a(x),b(x))
def val_func_power(function,n):
	A=function
	if n==1:return A
	return val_func_compose(A,val_func_power(A,n-1))
def val_func_matcher(function,target):return lambda x:function(x)==target
def val_func_other(container,value):return val_func_first(val_func_remove(value,container))
def val_func_remove(value,container):A=container;return type(A)(A for A in A if A!=value)
def val_func_first(container):return next(iter(container))
def val_func_sfilter(container,condition):A=container;return type(A)(A for A in A if condition(A))
def val_func_either(a,b):return a or b
def val_func_difference(a,b):return type(a)(A for A in a if A not in b)
def val_func_intersection(a,b):return a&b
def val_func_combine(a,b):return type(a)((*a,*b))
def p(I):J=False;I=tuple(map(tuple,I));K=val_func_palette(I);L=val_func_objects(I,J,J,True);M=val_func_ofcolor(I,0);B=val_func_first(L);N=val_func_ulcorner(B);C=val_func_subgrid(B,I);O=val_func_power(val_func_trim,2);P=O(C);Q=val_func_asindices(P);R=val_func_shift(Q,(2,2));D=val_func_fill(C,0,R);A=val_func_leastcolor(D);S=val_func_remove(0,K);T=val_func_other(S,A);U=val_func_ofcolor(D,A);E=val_func_shift(U,N);F=val_func_ofcolor(I,A);V=val_func_uppermost(F);W=val_func_lowermost(F);X=val_func_matcher(val_func_first,V);Y=val_func_matcher(val_func_first,W);Z=val_func_fork(val_func_either,X,Y);G=val_func_sfilter(E,Z);a=val_func_difference(E,G);b=mval_func_apply(val_func_vfrontier,G);c=mval_func_apply(val_func_hfrontier,a);H=val_func_combine(b,c);d=val_func_intersection(M,H);e=val_func_fill(I,T,H);f=val_func_fill(e,A,d);return[*map(list,f)]