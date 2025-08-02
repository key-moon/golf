def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_dmirror(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_crop(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def val_func_portrait(A):return val_func_height(A)>val_func_width(A)
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_height(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_branch(A,B,C):return B if A else C
def val_func_astuple(A,B):return A,B
def val_func_dedupe(A):return tuple(B for(C,B)in enumerate(A)if A.index(B)==C)
def val_func_identity(A):return A
def p(A):A=tuple(map(tuple,A));B=val_func_portrait(A);C=val_func_branch(B,val_func_dmirror,val_func_identity);D=val_func_branch(B,val_func_height,val_func_width);E=D(A);F=val_func_astuple(1,E);G=C(A);H=val_func_crop(G,(0,0),F);I=val_func_apply(val_func_dedupe,H);J=C(I);return[*map(list,J)]