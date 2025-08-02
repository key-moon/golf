def val_func_first(container):return next(iter(container))
def val_func_ival_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(loc):return dval_func_neighbors(loc)|val_func_ival_func_neighbors(loc)
def dval_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
def mostval_func_color(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_canvas(value,dimensions):A=dimensions;return tuple(tuple(value for A in range(A[1]))for B in range(A[0]))
def val_func_color(obj):return next(iter(obj))[0]
def val_func_palette(element):
	A=element
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_objects(grid,univalued,diagonal,without_bg):
	A=grid;H=mostval_func_color(A)if without_bg else None;I=set();D=set();L,M=len(A),len(A[0]);N=val_func_asindices(A);O=val_func_neighbors if diagonal else dval_func_neighbors
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
def val_func_other(container,value):return val_func_first(val_func_remove(value,container))
def val_func_remove(value,container):A=container;return type(A)(A for A in A if A!=value)
def val_func_argmax(container,compfunc):return max(container,key=compfunc)
def val_func_size(container):return len(container)
def p(I):I=tuple(map(tuple,I));A=val_func_palette(I);B=val_func_objects(I,True,False,True);C=val_func_argmax(B,val_func_size);D=val_func_color(C);E=val_func_remove(0,A);F=val_func_other(E,D);G=val_func_canvas(F,(1,1));return[*map(list,G)]