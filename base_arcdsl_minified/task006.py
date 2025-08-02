def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_lrcorner(A):return tuple(map(max,zip(*val_func_toindices(A))))
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_tophalf(A):return A[:len(A)//2]
def val_func_bottomhalf(A):return A[len(A)//2+len(A)%2:]
def val_func_rot270(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def val_func_rot90(A):return tuple(A for A in zip(*A[::-1]))
def val_func_righthalf(A):return val_func_rot270(val_func_bottomhalf(val_func_rot90(A)))
def val_func_lefthalf(A):return val_func_rot270(val_func_tophalf(val_func_rot90(A)))
def val_func_replace(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def val_func_cellwise(A,B,C):
	I,J=len(A),len(A[0]);D=tuple()
	for F in range(I):
		E=tuple()
		for G in range(J):H=A[F][G];K=H if H==B[F][G]else C;E=E+(K,)
		D=D+(E,)
	return D
def val_func_vmirror(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=val_func_ulcorner(A)[1]+val_func_lrcorner(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def p(A):A=tuple(map(tuple,A));B=val_func_vmirror(A);C=val_func_lefthalf(B);D=val_func_righthalf(B);E=val_func_vmirror(D);F=val_func_cellwise(C,E,0);G=val_func_replace(F,1,2);return[*map(list,G)]