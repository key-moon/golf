def pval_func_apply(A,B,C):return tuple(A(B,C)for(B,C)in zip(B,C))
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_paint(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def val_func_rot180(A):return tuple(tuple(A[::-1])for A in A[::-1])
def val_func_rot90(A):return tuple(A for A in zip(*A[::-1]))
def val_func_asobject(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_crop(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def mpval_func_apply(A,B,C):return val_func_merge(pval_func_apply(A,B,C))
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_astuple(A,B):return A,B
def val_func_tojvec(A):return 0,A
def p(A):A=tuple(map(tuple,A));B=val_func_crop(A,(0,0),(3,3));C=val_func_rot90(B);D=val_func_rot180(B);E=val_func_astuple(C,D);F=val_func_astuple(4,8);G=val_func_apply(val_func_tojvec,F);H=val_func_apply(val_func_asobject,E);I=mpval_func_apply(val_func_shift,H,G);J=val_func_paint(A,I);return[*map(list,J)]