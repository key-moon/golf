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
def val_func_vupscale(grid,factor):
	A=tuple()
	for B in grid:A=A+tuple(B for A in range(factor))
	return A
def val_func_hupscale(grid,factor):
	A=tuple()
	for C in grid:
		B=tuple()
		for D in C:B=B+tuple(D for A in range(factor))
		A=A+(B,)
	return A
def val_func_rot90(grid):return tuple(A for A in zip(*grid[::-1]))
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
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_branch(condition,a,b):return a if condition else b
def val_func_mostcommon(container):A=container;return max(set(A),key=A.count)
def val_func_size(container):return len(container)
def val_func_greater(a,b):return a>b
def val_func_repeat(item,num):return tuple(item for A in range(num))
def val_func_dedupe(tup):return tuple(A for(B,A)in enumerate(tup)if tup.index(A)==B)
def p(I):I=tuple(map(tuple,I));E=val_func_rot90(I);B=val_func_apply(val_func_mostcommon,I);C=val_func_apply(val_func_mostcommon,E);F=val_func_repeat(B,1);G=val_func_repeat(C,1);D=val_func_compose(val_func_size,val_func_dedupe);H=D(B);J=D(C);A=val_func_greater(J,H);K=val_func_branch(A,val_func_height,val_func_width);L=K(I);M=val_func_rot90(F);N=val_func_branch(A,G,M);O=val_func_branch(A,val_func_vupscale,val_func_hupscale);P=O(N,L);return[*map(list,P)]