def val_func_ival_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(loc):return dval_func_neighbors(loc)|val_func_ival_func_neighbors(loc)
def dval_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
def mostval_func_color(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_manhattan(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in val_func_toindices(a)for(C,D)in val_func_toindices(b))
def val_func_canvas(value,dimensions):A=dimensions;return tuple(tuple(value for A in range(A[1]))for B in range(A[0]))
def val_func_color(obj):return next(iter(obj))[0]
def val_func_adjacent(a,b):return val_func_manhattan(a,b)==1
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
def val_func_rbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def val_func_remove(value,container):A=container;return type(A)(A for A in A if A!=value)
def val_func_extract(container,condition):return next(A for A in container if condition(A))
def val_func_argmin(container,compfunc):return min(container,key=compfunc)
def val_func_size(container):return len(container)
def p(I):C=False;I=tuple(map(tuple,I));A=val_func_objects(I,True,C,C);B=val_func_argmin(A,val_func_size);D=val_func_rbind(val_func_adjacent,B);E=val_func_remove(B,A);F=val_func_extract(E,D);G=val_func_color(F);H=val_func_canvas(G,(1,1));return[*map(list,H)]