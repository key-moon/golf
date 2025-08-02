def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
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
def val_func_bordering(A,B):return val_func_uppermost(A)==0 or val_func_leftmost(A)==0 or val_func_lowermost(A)==len(B)-1 or val_func_rightmost(A)==len(B[0])-1
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_rbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(D,B)
	elif C==3:return lambda D,E:A(D,E,B)
	else:return lambda D,E,F:A(D,E,F,B)
def val_func_mfilter(A,B):return val_func_merge(val_func_sfilter(A,B))
def val_func_initset(A):return frozenset({A})
def p(A):A=tuple(map(tuple,A));B=val_func_asindices(A);C=val_func_apply(val_func_initset,B);D=val_func_rbind(val_func_bordering,A);E=val_func_mfilter(C,D);F=val_func_fill(A,8,E);return[*map(list,F)]