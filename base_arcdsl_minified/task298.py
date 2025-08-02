def pval_func_apply(A,B,C):return tuple(A(B,C)for(B,C)in zip(B,C))
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_palette(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_paint(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def val_func_color(A):return next(iter(A))[0]
def val_func_partition(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in val_func_palette(A))
def reval_func_color(A,B):return frozenset((A,B)for B in val_func_toindices(B))
def mpval_func_apply(A,B,C):return val_func_merge(pval_func_apply(A,B,C))
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_remove(A,B):return type(B)(B for B in B if B!=A)
def val_func_last(A):return max(enumerate(A))[1]
def val_func_size(A):return len(A)
def val_func_repeat(A,B):return tuple(A for B in range(B))
def val_func_order(A,B):return tuple(sorted(A,key=B))
def val_func_combine(A,B):return type(A)((*A,*B))
def p(A):A=tuple(map(tuple,A));D=val_func_partition(A);B=val_func_order(D,val_func_size);E=val_func_apply(val_func_color,B);C=val_func_last(B);F=val_func_remove(C,B);G=val_func_repeat(C,1);H=val_func_combine(G,F);I=mpval_func_apply(reval_func_color,E,H);J=val_func_paint(A,I);return[*map(list,J)]