def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_lrcorner(patch):return tuple(map(max,zip(*val_func_toindices(patch))))
def val_func_ulcorner(patch):return tuple(map(min,zip(*val_func_toindices(patch))))
def val_func_tophalf(grid):return grid[:len(grid)//2]
def val_func_bottomhalf(grid):A=grid;return A[len(A)//2+len(A)%2:]
def val_func_rot270(grid):return tuple(tuple(A[::-1])for A in zip(*grid[::-1]))[::-1]
def val_func_rot90(grid):return tuple(A for A in zip(*grid[::-1]))
def val_func_righthalf(grid):return val_func_rot270(val_func_bottomhalf(val_func_rot90(grid)))
def val_func_lefthalf(grid):return val_func_rot270(val_func_tophalf(val_func_rot90(grid)))
def val_func_replace(grid,val_func_replacee,val_func_replacer):return tuple(tuple(val_func_replacer if A==val_func_replacee else A for A in A)for A in grid)
def val_func_cellwise(a,b,fallback):
	F,G=len(a),len(a[0]);A=tuple()
	for C in range(F):
		B=tuple()
		for D in range(G):E=a[C][D];H=E if E==b[C][D]else fallback;B=B+(H,)
		A=A+(B,)
	return A
def val_func_vmirror(piece):
	A=piece
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=val_func_ulcorner(A)[1]+val_func_lrcorner(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def p(I):I=tuple(map(tuple,I));A=val_func_vmirror(I);B=val_func_lefthalf(A);C=val_func_righthalf(A);D=val_func_vmirror(C);E=val_func_cellwise(B,D,0);F=val_func_replace(E,1,2);return[*map(list,F)]