def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_rot270(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def val_func_rot90(A):return tuple(A for A in zip(*A[::-1]))
def val_func_righthalf(A):return val_func_rot270(val_func_bottomhalf(val_func_rot90(A)))
def val_func_lefthalf(A):return val_func_rot270(val_func_tophalf(val_func_rot90(A)))
def val_func_bottomhalf(A):return A[len(A)//2+len(A)%2:]
def val_func_tophalf(A):return A[:len(A)//2]
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def p(A):A=tuple(map(tuple,A));B=val_func_tophalf(A);C=val_func_bottomhalf(A);D=val_func_lefthalf(B);E=val_func_righthalf(B);F=val_func_lefthalf(C);G=val_func_righthalf(C);H=val_func_ofcolor(E,4);I=val_func_ofcolor(D,7);J=val_func_ofcolor(F,8);K=val_func_fill(G,8,J);L=val_func_fill(K,4,H);M=val_func_fill(L,7,I);return[*map(list,M)]