def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_mostcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_underfill(A,B,C):
	G,H=len(A),len(A[0]);I=val_func_mostcolor(A);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_urcorner(A):return tuple(map(lambda B:{0:min,1:max}[B[0]](B[1]),enumerate(zip(*val_func_toindices(A)))))
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_fork(A,B,C):return lambda D:A(B(D),C(D))
def val_func_power(A,B):
	if B==1:return A
	return val_func_compose(A,val_func_power(A,B-1))
def val_func_product(A,B):return frozenset((C,B)for B in B for C in A)
def val_func_astuple(A,B):return A,B
def val_func_remove(A,B):return type(B)(B for B in B if B!=A)
def val_func_last(A):return max(enumerate(A))[1]
def val_func_first(A):return next(iter(A))
def p(A):A=tuple(map(tuple,A));B=val_func_ofcolor(A,5);C=val_func_product(B,B);D=val_func_power(val_func_first,2);E=val_func_power(val_func_last,2);F=val_func_fork(val_func_astuple,D,E);G=val_func_apply(F,C);H=val_func_urcorner(B);I=val_func_remove(H,G);J=val_func_underfill(A,2,I);return[*map(list,J)]