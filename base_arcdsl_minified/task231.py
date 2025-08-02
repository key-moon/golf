def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
def val_func_normalize(A):
	if len(A)==0:return A
	return val_func_shift(A,(-val_func_uppermost(A),-val_func_leftmost(A)))
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_hperiod(A):
	B=val_func_normalize(A);C=val_func_width(B)
	for D in range(1,C):
		E=val_func_shift(B,(0,-D));F=frozenset({(B,(C,A))for(B,(C,A))in E if A>=0})
		if F.issubset(B):return D
	return C
def val_func_rot270(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def val_func_rot90(A):return tuple(A for A in zip(*A[::-1]))
def val_func_asobject(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def val_func_crop(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_height(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def val_func_astuple(A,B):return A,B
def val_func_increment(A):return A+1 if isinstance(A,int)else(A[0]+1,A[1]+1)
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_repeat(A,B):return tuple(A for B in range(B))
def val_func_double(A):return A*2 if isinstance(A,int)else(A[0]*2,A[1]*2)
def val_func_divide(A,B):
	if isinstance(A,int)and isinstance(B,int):return A//B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]//B[0],A[1]//B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A//B[0],A//B[1]
	return A[0]//B,A[1]//B
def p(A):A=tuple(map(tuple,A));F=val_func_width(A);B=val_func_asobject(A);C=val_func_hperiod(B);D=val_func_height(B);G=val_func_astuple(D,C);H=val_func_ulcorner(B);I=val_func_crop(A,H,G);J=val_func_rot90(I);E=val_func_double(F);K=val_func_divide(E,C);L=val_func_increment(K);M=val_func_repeat(J,L);N=val_func_merge(M);O=val_func_rot270(N);P=val_func_astuple(D,E);Q=val_func_crop(O,(0,0),P);return[*map(list,Q)]