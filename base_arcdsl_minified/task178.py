def ival_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(loc):return val_func_dval_func_neighbors(loc)|ival_func_neighbors(loc)
def val_func_dval_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
def val_func_mostval_func_color(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
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
def val_func_dmirror(piece):
	A=piece
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_color(obj):return next(iter(obj))[0]
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
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
def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_chain(h,g,f):return lambda x:h(g(f(x)))
def val_func_branch(condition,a,b):return a if condition else b
def val_func_first(container):return next(iter(container))
def val_func_size(container):return len(container)
def val_func_repeat(item,num):return tuple(item for A in range(num))
def val_func_order(container,compfunc):return tuple(sorted(container,key=compfunc))
def val_func_dedupe(tup):return tuple(A for(B,A)in enumerate(tup)if tup.index(A)==B)
def val_func_equality(a,b):return a==b
def val_func_identity(x):return x
def p(I):B=False;I=tuple(map(tuple,I));C=val_func_chain(val_func_size,val_func_dedupe,val_func_first);D=C(I);E=val_func_equality(D,1);A=val_func_branch(E,val_func_dmirror,val_func_identity);F=A(I);G=val_func_objects(F,True,B,B);H=val_func_order(G,val_func_leftmost);J=val_func_apply(val_func_color,H);K=val_func_repeat(J,1);L=A(K);return[*map(list,L)]