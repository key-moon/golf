def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_replace(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_toobject(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in val_func_toindices(A)if 0<=A<D and 0<=C<E)
def val_func_dneighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_colorcount(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def val_func_leastcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def val_func_rbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(D,B)
	elif C==3:return lambda D,E:A(D,E,B)
	else:return lambda D,E,F:A(D,E,F,B)
def val_func_chain(A,B,C):return lambda D:A(B(C(D)))
def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_positive(A):return A>0
def val_func_decrement(A):return A-1 if isinstance(A,int)else(A[0]-1,A[1]-1)
def p(A):A=tuple(map(tuple,A));C=val_func_leastcolor(A);E=val_func_ofcolor(A,C);B=val_func_replace(A,C,0);D=val_func_leastcolor(B);F=val_func_rbind(val_func_colorcount,D);G=val_func_chain(val_func_positive,val_func_decrement,F);H=val_func_rbind(val_func_toobject,B);I=val_func_chain(G,H,val_func_dneighbors);J=val_func_sfilter(E,I);K=val_func_fill(B,D,J);return[*map(list,K)]