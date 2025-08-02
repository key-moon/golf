def val_func_shift(patch,directions):
	A=patch
	if len(A)==0:return A
	B,C=directions
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(D+B,E+C))for(A,(D,E))in A)
	return frozenset((A+B,D+C)for(A,D)in A)
def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
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
def val_func_replace(grid,val_func_replacee,val_func_replacer):return tuple(tuple(val_func_replacer if A==val_func_replacee else A for A in A)for A in grid)
def val_func_subgrid(patch,grid):A=patch;return val_func_crop(grid,val_func_ulcorner(A),val_func_shape(A))
def val_func_upscale(element,factor):
	B=element;A=factor
	if isinstance(B,tuple):
		C=tuple()
		for I in B:
			D=tuple()
			for E in I:D=D+tuple(E for A in range(A))
			C=C+tuple(D for A in range(A))
		return C
	else:
		if len(B)==0:return frozenset()
		F,G=val_func_ulcorner(B);J,K=-F,-G;L=val_func_shift(B,(J,K));H=set()
		for(E,(M,N))in L:
			for O in range(A):
				for P in range(A):H.add((E,(M*A+O,N*A+P)))
		return val_func_shift(frozenset(H),(F,G))
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def p(I):I=tuple(map(tuple,I));A=val_func_ofcolor(I,3);B=val_func_subgrid(A,I);C=val_func_ofcolor(B,0);D=val_func_replace(I,3,0);E=val_func_replace(D,8,0);F=val_func_compress(E);G=val_func_upscale(F,3);H=val_func_fill(G,0,C);return[*map(list,H)]