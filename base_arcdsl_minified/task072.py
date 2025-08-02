def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_bottomhalf(A):return A[len(A)//2+len(A)%2:]
def val_func_tophalf(A):return A[:len(A)//2]
def val_func_canvas(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_astuple(A,B):return A,B
def val_func_difference(A,B):return type(A)(A for A in A if A not in B)
def val_func_intersection(A,B):return A&B
def val_func_combine(A,B):return type(A)((*A,*B))
def p(A):A=tuple(map(tuple,A));D=val_func_tophalf(A);E=val_func_bottomhalf(A);F=val_func_astuple(6,5);B=val_func_ofcolor(D,2);C=val_func_ofcolor(E,2);G=val_func_combine(B,C);H=val_func_intersection(B,C);I=val_func_difference(G,H);J=val_func_canvas(0,F);K=val_func_fill(J,3,I);return[*map(list,K)]