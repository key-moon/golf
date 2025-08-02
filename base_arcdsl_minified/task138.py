def val_func_sfilter(container,condition):A=container;return type(A)(A for A in A if condition(A))
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def ival_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(loc):return val_func_dval_func_neighbors(loc)|ival_func_neighbors(loc)
def val_func_dval_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
def val_func_palette(element):
	A=element
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_mostval_func_color(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
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
def val_func_ulcorner(patch):return tuple(map(min,zip(*val_func_toindices(patch))))
def val_func_shape(piece):A=piece;return val_func_height(A),val_func_width(A)
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
def val_func_outbox(patch):A=patch;F,G=val_func_uppermost(A)-1,val_func_leftmost(A)-1;H,I=val_func_lowermost(A)+1,val_func_rightmost(A)+1;B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def val_func_connect(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def val_func_subgrid(patch,grid):A=patch;return val_func_crop(grid,val_func_ulcorner(A),val_func_shape(A))
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_color(obj):return next(iter(obj))[0]
def val_func_bordering(patch,grid):A=patch;return val_func_uppermost(A)==0 or val_func_leftmost(A)==0 or val_func_lowermost(A)==len(grid)-1 or val_func_rightmost(A)==len(grid[0])-1
def val_func_hline(patch):A=patch;return val_func_width(A)==len(A)and val_func_height(A)==1
def val_func_vline(patch):A=patch;return val_func_height(A)==len(A)and val_func_width(A)==1
def val_func_fgpartition(grid):A=grid;return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in val_func_palette(A)-{val_func_mostval_func_color(A)})
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
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_val_func_colorfilter(objs,value):return frozenset(A for A in objs if next(iter(A))[0]==value)
def val_func_prapply(function,a,b):return frozenset(function(B,A)for A in b for B in a)
def val_func_rbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_branch(condition,a,b):return a if condition else b
def val_func_extract(container,condition):return next(A for A in container if condition(A))
def val_func_mfilter(container,function):return val_func_merge(val_func_sfilter(container,function))
def val_func_argmax(container,compfunc):return max(container,key=compfunc)
def val_func_size(container):return len(container)
def val_func_greater(a,b):return a>b
def val_func_flip(b):return not b
def p(I):G=False;I=tuple(map(tuple,I));H=val_func_objects(I,True,G,G);J=val_func_val_func_colorfilter(H,0);K=val_func_rbind(val_func_bordering,I);L=val_func_compose(val_func_flip,K);M=val_func_extract(J,L);N=val_func_outbox(M);A=val_func_subgrid(N,I);O=val_func_fgpartition(A);B=val_func_argmax(O,val_func_size);P=val_func_color(B);C=val_func_toindices(B);D=val_func_prapply(val_func_connect,C,C);E=val_func_mfilter(D,val_func_vline);F=val_func_mfilter(D,val_func_hline);Q=val_func_size(E);R=val_func_size(F);S=val_func_greater(Q,R);T=val_func_branch(S,E,F);U=val_func_fill(A,P,T);return[*map(list,U)]