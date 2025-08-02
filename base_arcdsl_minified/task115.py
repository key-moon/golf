def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
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
def val_func_dmirror(piece):
	A=piece
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_crop(grid,start,dims):A=start;return tuple(B[A[1]:A[1]+dims[1]]for B in grid[A[0]:A[0]+dims[0]])
def val_func_portrait(piece):A=piece;return val_func_height(A)>val_func_width(A)
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
def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_branch(condition,a,b):return a if condition else b
def val_func_astuple(a,b):return a,b
def val_func_dedupe(tup):return tuple(A for(B,A)in enumerate(tup)if tup.index(A)==B)
def val_func_identity(x):return x
def p(I):I=tuple(map(tuple,I));A=val_func_portrait(I);B=val_func_branch(A,val_func_dmirror,val_func_identity);C=val_func_branch(A,val_func_height,val_func_width);D=C(I);E=val_func_astuple(1,D);F=B(I);G=val_func_crop(F,(0,0),E);H=val_func_apply(val_func_dedupe,G);J=B(H);return[*map(list,J)]