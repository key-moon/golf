def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_fork(A,B,C):return lambda D:A(B(D),C(D))
def val_func_rbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(D,B)
	elif C==3:return lambda D,E:A(D,E,B)
	else:return lambda D,E,F:A(D,E,F,B)
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_last(A):return max(enumerate(A))[1]
def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_equality(A,B):return A==B
def val_func_divide(A,B):
	if isinstance(A,int)and isinstance(B,int):return A//B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]//B[0],A[1]//B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A//B[0],A//B[1]
	return A[0]//B,A[1]//B
def val_func_multiply(A,B):
	if isinstance(A,int)and isinstance(B,int):return A*B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]*B[0],A[1]*B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A*B[0],A*B[1]
	return A[0]*B,A[1]*B
def val_func_identity(A):return A
def p(A):A=tuple(map(tuple,A));B=val_func_rbind(val_func_divide,3);C=val_func_rbind(val_func_multiply,3);D=val_func_compose(C,B);E=val_func_fork(val_func_equality,val_func_identity,D);F=val_func_compose(E,val_func_last);G=val_func_ofcolor(A,4);H=val_func_sfilter(G,F);I=val_func_fill(A,6,H);return[*map(list,I)]