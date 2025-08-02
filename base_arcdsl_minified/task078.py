def val_func_lrcorner(A):return tuple(map(max,zip(*val_func_toindices(A))))
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_dmirror(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_vmirror(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=val_func_ulcorner(A)[1]+val_func_lrcorner(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def val_func_switch(A,B,C):return tuple(tuple(A if A!=B and A!=C else{B:C,C:B}[A]for A in A)for A in A)
def val_func_cmirror(A):
	if isinstance(A,tuple):return tuple(zip(*(A[::-1]for A in A[::-1])))
	return val_func_vmirror(val_func_dmirror(val_func_vmirror(A)))
def val_func_rot270(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_rbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(D,B)
	elif C==3:return lambda D,E:A(D,E,B)
	else:return lambda D,E,F:A(D,E,F,B)
def val_func_order(A,B):return tuple(sorted(A,key=B))
def val_func_identity(A):return A
def p(A):A=tuple(map(tuple,A));B=val_func_rot270(A);C=val_func_rbind(val_func_order,val_func_identity);D=val_func_switch(B,1,2);E=val_func_apply(C,D);F=val_func_switch(E,1,2);G=val_func_cmirror(F);return[*map(list,G)]