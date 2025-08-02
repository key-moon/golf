def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_canvas(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_crop(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_leastcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def mval_func_apply(A,B):return val_func_merge(val_func_apply(A,B))
def val_func_rbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(D,B)
	elif C==3:return lambda D,E:A(D,E,B)
	else:return lambda D,E,F:A(D,E,F,B)
def val_func_astuple(A,B):return A,B
def val_func_tojvec(A):return 0,A
def val_func_combine(A,B):return type(A)((*A,*B))
def p(A):A=tuple(map(tuple,A));B=val_func_leastcolor(A);C=val_func_crop(A,(0,0),(3,3));D=val_func_crop(A,(2,0),(3,3));E=val_func_tojvec(4);F=val_func_crop(A,E,(3,3));G=val_func_astuple(2,4);H=val_func_crop(A,G,(3,3));I=val_func_canvas(0,(3,3));J=val_func_rbind(val_func_ofcolor,B);K=val_func_astuple(C,D);L=val_func_astuple(F,H);M=val_func_combine(K,L);N=mval_func_apply(J,M);O=val_func_fill(I,B,N);return[*map(list,O)]