def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_vupscale(A,B):
	C=tuple()
	for D in A:C=C+tuple(D for A in range(B))
	return C
def val_func_hupscale(A,B):
	C=tuple()
	for E in A:
		D=tuple()
		for F in E:D=D+tuple(F for A in range(B))
		C=C+(D,)
	return C
def val_func_rot90(A):return tuple(A for A in zip(*A[::-1]))
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_height(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_branch(A,B,C):return B if A else C
def val_func_mostcommon(A):return max(set(A),key=A.count)
def val_func_size(A):return len(A)
def val_func_greater(A,B):return A>B
def val_func_repeat(A,B):return tuple(A for B in range(B))
def val_func_dedupe(A):return tuple(B for(C,B)in enumerate(A)if A.index(B)==C)
def p(A):A=tuple(map(tuple,A));F=val_func_rot90(A);C=val_func_apply(val_func_mostcommon,A);D=val_func_apply(val_func_mostcommon,F);G=val_func_repeat(C,1);H=val_func_repeat(D,1);E=val_func_compose(val_func_size,val_func_dedupe);I=E(C);J=E(D);B=val_func_greater(J,I);K=val_func_branch(B,val_func_height,val_func_width);L=K(A);M=val_func_rot90(G);N=val_func_branch(B,H,M);O=val_func_branch(B,val_func_vupscale,val_func_hupscale);P=O(N,L);return[*map(list,P)]