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
def val_func_replace(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def val_func_paint(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def val_func_toobject(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in val_func_toindices(A)if 0<=A<D and 0<=C<E)
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_recolor(A,B):return frozenset((A,B)for B in val_func_toindices(B))
def val_func_crop(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def mval_func_apply(A,B):return val_func_merge(val_func_apply(A,B))
def val_func_lbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(B,D)
	elif C==3:return lambda D,E:A(B,D,E)
	else:return lambda D,E,F:A(B,D,E,F)
def val_func_branch(A,B,C):return B if A else C
def val_func_product(A,B):return frozenset((C,B)for B in B for C in A)
def val_func_astuple(A,B):return A,B
def val_func_insert(A,B):return B.union(frozenset({A}))
def val_func_last(A):return max(enumerate(A))[1]
def val_func_first(A):return next(iter(A))
def val_func_initset(A):return frozenset({A})
def val_func_greater(A,B):return A>B
def val_func_multiply(A,B):
	if isinstance(A,int)and isinstance(B,int):return A*B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]*B[0],A[1]*B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A*B[0],A*B[1]
	return A[0]*B,A[1]*B
def p(A):A=tuple(map(tuple,A));G=val_func_ofcolor(A,4);C=val_func_first(G);D=val_func_first(C);E=val_func_last(C);H=val_func_greater(D,3);I=val_func_greater(D,7);J=val_func_greater(E,3);K=val_func_greater(E,7);L=val_func_branch(H,4,0);M=val_func_branch(I,8,L);N=val_func_branch(J,4,0);O=val_func_branch(K,8,N);P=val_func_astuple(M,O);Q=val_func_initset(0);R=val_func_insert(4,Q);F=val_func_insert(8,R);S=val_func_product(F,F);T=val_func_crop(A,(0,0),(3,3));U=val_func_asindices(T);V=val_func_recolor(0,U);W=val_func_lbind(val_func_shift,V);X=mval_func_apply(W,S);Y=val_func_paint(A,X);Z=val_func_crop(A,P,(3,3));B=val_func_replace(Z,5,0);a=val_func_ofcolor(B,4);b=val_func_first(a);c=val_func_asindices(B);d=val_func_toobject(c,B);e=val_func_multiply(b,4);f=val_func_shift(d,e);g=val_func_paint(Y,f);return[*map(list,g)]