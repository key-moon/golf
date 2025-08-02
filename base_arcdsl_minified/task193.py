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
def val_func_dneighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_leastcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def val_func_rbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(D,B)
	elif C==3:return lambda D,E:A(D,E,B)
	else:return lambda D,E,F:A(D,E,F,B)
def val_func_chain(A,B,C):return lambda D:A(B(C(D)))
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_size(A):return len(A)
def val_func_greater(A,B):return A>B
def val_func_difference(A,B):return type(A)(A for A in A if A not in B)
def p(A):A=tuple(map(tuple,A));C=val_func_leastcolor(A);B=val_func_ofcolor(A,C);D=val_func_rbind(val_func_difference,B);E=val_func_rbind(val_func_greater,2);F=val_func_chain(E,val_func_size,D);G=val_func_compose(F,val_func_dneighbors);H=val_func_sfilter(B,G);I=val_func_fill(A,0,H);return[*map(list,I)]