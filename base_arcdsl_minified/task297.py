def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
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
def val_func_tophalf(grid):return grid[:len(grid)//2]
def val_func_vconcat(a,b):return a+b
def val_func_hupscale(grid,factor):
	A=tuple()
	for C in grid:
		B=tuple()
		for D in C:B=B+tuple(D for A in range(factor))
		A=A+(B,)
	return A
def val_func_dmirror(piece):
	A=piece
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_crop(grid,start,dims):A=start;return tuple(B[A[1]:A[1]+dims[1]]for B in grid[A[0]:A[0]+dims[0]])
def val_func_width(piece):
	A=piece
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_astuple(a,b):return a,b
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_repeat(item,num):return tuple(item for A in range(num))
def p(I):I=tuple(map(tuple,I));A=val_func_width(I);C=val_func_astuple(2,A);B=val_func_crop(I,(0,0),C);D=val_func_tophalf(B);E=val_func_dmirror(D);F=val_func_hupscale(E,A);G=val_func_repeat(F,2);H=val_func_merge(G);J=val_func_vconcat(B,H);return[*map(list,J)]