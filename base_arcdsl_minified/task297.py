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
def val_func_tophalf(A):return A[:len(A)//2]
def val_func_vconcat(A,B):return A+B
def val_func_hupscale(A,B):
	C=tuple()
	for E in A:
		D=tuple()
		for F in E:D=D+tuple(F for A in range(B))
		C=C+(D,)
	return C
def val_func_dmirror(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_crop(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_astuple(A,B):return A,B
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_repeat(A,B):return tuple(A for B in range(B))
def p(A):A=tuple(map(tuple,A));B=val_func_width(A);D=val_func_astuple(2,B);C=val_func_crop(A,(0,0),D);E=val_func_tophalf(C);F=val_func_dmirror(E);G=val_func_hupscale(F,B);H=val_func_repeat(G,2);I=val_func_merge(H);J=val_func_vconcat(C,I);return[*map(list,J)]