def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
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
def val_func_vfrontier(location):return frozenset((A,location[1])for A in range(30))
def val_func_center(patch):A=patch;return val_func_uppermost(A)+val_func_height(A)//2,val_func_leftmost(A)+val_func_width(A)//2
def val_func_underfill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);G=val_func_mostval_func_color(A);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:
			if B[C][D]==G:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_color(obj):return next(iter(obj))[0]
def val_func_vmatching(a,b):return len(set(A for(B,A)in val_func_toindices(a))&set(A for(B,A)in val_func_toindices(b)))>0
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
def mval_func_apply(function,container):return val_func_merge(val_func_apply(function,container))
def val_func_fork(outer,a,b):return lambda x:outer(a(x),b(x))
def val_func_rbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def val_func_chain(h,g,f):return lambda x:h(g(f(x)))
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_remove(value,container):A=container;return type(A)(A for A in A if A!=value)
def val_func_first(container):return next(iter(container))
def val_func_sfilter(container,condition):A=container;return type(A)(A for A in A if condition(A))
def val_func_increment(x):return x+1 if isinstance(x,int)else(x[0]+1,x[1]+1)
def val_func_both(a,b):return a and b
def val_func_argmax(container,compfunc):return max(container,key=compfunc)
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_size(container):return len(container)
def val_func_greater(a,b):return a>b
def p(I):B=True;I=tuple(map(tuple,I));C=val_func_objects(I,B,B,B);A=val_func_argmax(C,val_func_size);D=val_func_remove(A,C);F=val_func_merge(D);G=val_func_color(F);E=val_func_uppermost(A);H=val_func_rbind(val_func_greater,E);J=val_func_compose(H,val_func_uppermost);K=val_func_rbind(val_func_vmatching,A);L=val_func_fork(val_func_both,K,J);M=val_func_sfilter(D,L);N=val_func_increment(E);O=val_func_rbind(val_func_greater,N);P=val_func_compose(O,val_func_first);Q=val_func_rbind(val_func_sfilter,P);R=val_func_chain(Q,val_func_vfrontier,val_func_center);S=mval_func_apply(R,M);T=val_func_underfill(I,G,S);return[*map(list,T)]