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
def val_func_compress(grid):A=grid;B=tuple(A for(A,B)in enumerate(A)if len(set(B))==1);C=tuple(A for(A,B)in enumerate(val_func_dmirror(A))if len(set(B))==1);return tuple(tuple(B for(A,B)in enumerate(D)if A not in C)for(A,D)in enumerate(A)if A not in B)
def val_func_canvas(value,dimensions):A=dimensions;return tuple(tuple(value for A in range(A[1]))for B in range(A[0]))
def val_func_palette(element):
	A=element
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_crop(grid,start,dims):A=start;return tuple(B[A[1]:A[1]+dims[1]]for B in grid[A[0]:A[0]+dims[0]])
def val_func_colorcount(element,value):
	B=value;A=element
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_lbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def val_func_rbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_astuple(a,b):return a,b
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_order(container,compfunc):return tuple(sorted(container,key=compfunc))
def val_func_invert(n):return-n if isinstance(n,int)else(-n[0],-n[1])
def p(I):I=tuple(map(tuple,I));A=val_func_compress(I);B=val_func_astuple(3,1);C=val_func_palette(A);D=val_func_lbind(val_func_colorcount,A);E=val_func_compose(val_func_invert,D);F=val_func_order(C,E);G=val_func_rbind(val_func_canvas,(1,1));H=val_func_apply(G,F);J=val_func_merge(H);K=val_func_crop(J,(1,0),B);return[*map(list,K)]