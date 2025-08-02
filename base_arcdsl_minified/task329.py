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
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
def val_func_width(piece):
	A=piece
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_matcher(function,target):return lambda x:function(x)==target
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_last(container):return max(enumerate(container))[1]
def val_func_sfilter(container,condition):A=container;return type(A)(A for A in A if condition(A))
def val_func_flip(b):return not b
def val_func_halve(n):return n//2 if isinstance(n,int)else(n[0]//2,n[1]//2)
def p(I):I=tuple(map(tuple,I));A=val_func_asindices(I);B=val_func_width(I);C=val_func_halve(B);D=val_func_matcher(val_func_last,C);E=val_func_compose(val_func_flip,D);F=val_func_sfilter(A,E);G=val_func_fill(I,0,F);return[*map(list,G)]