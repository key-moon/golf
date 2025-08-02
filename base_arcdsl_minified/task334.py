def val_func_remove(A,B):return type(B)(B for B in B if B!=A)
def val_func_first(A):return next(iter(A))
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_hfrontier(A):return frozenset((A[0],B)for B in range(30))
def val_func_vfrontier(A):return frozenset((B,A[1])for B in range(30))
def val_func_canvas(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_palette(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_fork(A,B,C):return lambda D:A(B(D),C(D))
def val_func_branch(A,B,C):return B if A else C
def val_func_other(A,B):return val_func_first(val_func_remove(B,A))
def val_func_combine(A,B):return type(A)((*A,*B))
def val_func_equality(A,B):return A==B
def p(A):A=tuple(map(tuple,A));C=val_func_palette(A);B=val_func_other(C,0);D=val_func_equality(B,1);E=val_func_equality(B,2);F=val_func_branch(D,(1,1),(2,2));G=val_func_branch(E,(0,1),F);H=val_func_fork(val_func_combine,val_func_vfrontier,val_func_hfrontier);I=H(G);J=val_func_canvas(0,(3,3));K=val_func_fill(J,5,I);return[*map(list,K)]