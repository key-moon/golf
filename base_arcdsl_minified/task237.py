def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def ival_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(loc):return val_func_dval_func_neighbors(loc)|ival_func_neighbors(loc)
def val_func_dval_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
def val_func_mostval_func_color(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
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
def val_func_shoot(start,direction):B=direction;A=start;return val_func_connect(A,(A[0]+42*B[0],A[1]+42*B[1]))
def val_func_connect(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def val_func_center(patch):A=patch;return val_func_uppermost(A)+val_func_height(A)//2,val_func_leftmost(A)+val_func_width(A)//2
def underval_func_paint(grid,obj):
	A=grid;E,F=len(A),len(A[0]);G=val_func_mostval_func_color(A);B=list(list(A)for A in A)
	for(H,(C,D))in obj:
		if 0<=C<E and 0<=D<F:
			if B[C][D]==G:B[C][D]=H
	return tuple(tuple(A)for A in B)
def val_func_paint(grid,obj):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(G,(C,D))in obj:
		if 0<=C<E and 0<=D<F:B[C][D]=G
	return tuple(tuple(A)for A in B)
def val_func_color(obj):return next(iter(obj))[0]
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
def val_func_objects(grid,univalued,diagonal,without_bg):
	A=grid;H=val_func_mostval_func_color(A)if without_bg else None;I=set();D=set();L,M=len(A),len(A[0]);N=val_func_asindices(A);O=val_func_neighbors if diagonal else val_func_dval_func_neighbors
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
def val_func_reval_func_color(value,patch):return frozenset((value,A)for A in val_func_toindices(patch))
def val_func_lrcorner(patch):return tuple(map(max,zip(*val_func_toindices(patch))))
def val_func_shape(piece):A=piece;return val_func_height(A),val_func_width(A)
def mval_func_apply(function,container):return val_func_merge(val_func_apply(function,container))
def val_func_fork(outer,a,b):return lambda x:outer(a(x),b(x))
def val_func_rbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_pair(a,b):return tuple(zip(a,b))
def val_func_remove(value,container):A=container;return type(A)(A for A in A if A!=value)
def val_func_insert(value,container):return container.union(frozenset({value}))
def val_func_last(container):return max(enumerate(container))[1]
def val_func_first(container):return next(iter(container))
def val_func_initset(value):return frozenset({value})
def val_func_order(container,compfunc):return tuple(sorted(container,key=compfunc))
def val_func_add(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):E=False;A=True;I=tuple(map(tuple,I));F=val_func_shape(I);G=val_func_objects(I,A,E,A);H=val_func_rbind(val_func_shoot,(0,1));J=val_func_compose(H,val_func_center);K=val_func_fork(val_func_reval_func_color,val_func_color,J);L=mval_func_apply(K,G);C=val_func_paint(I,L);M=val_func_add(F,(1,-1));N=val_func_initset(M);D=val_func_reval_func_color(0,N);O=val_func_objects(C,A,E,A);P=val_func_insert(D,O);B=val_func_order(P,val_func_uppermost);Q=val_func_first(B);R=val_func_remove(D,B);S=val_func_remove(Q,B);T=val_func_compose(val_func_lrcorner,val_func_first);U=val_func_compose(val_func_lrcorner,val_func_last);V=val_func_fork(val_func_connect,T,U);W=val_func_compose(val_func_color,val_func_first);X=val_func_fork(val_func_reval_func_color,W,V);Y=val_func_pair(R,S);Z=mval_func_apply(X,Y);a=underval_func_paint(C,Z);return[*map(list,a)]