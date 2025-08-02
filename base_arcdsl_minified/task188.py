def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
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
def val_func_rot270(grid):return tuple(tuple(A[::-1])for A in zip(*grid[::-1]))[::-1]
def val_func_rot90(grid):return tuple(A for A in zip(*grid[::-1]))
def val_func_lefthalf(grid):return val_func_rot270(val_func_tophalf(val_func_rot90(grid)))
def val_func_tophalf(grid):return grid[:len(grid)//2]
def val_func_portrait(piece):A=piece;return val_func_height(A)>val_func_width(A)
def val_func_branch(condition,a,b):return a if condition else b
def p(I):I=tuple(map(tuple,I));A=val_func_portrait(I);B=val_func_branch(A,val_func_tophalf,val_func_lefthalf);C=B(I);return[*map(list,C)]