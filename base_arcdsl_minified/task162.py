def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_upscale(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for I in A:
			D=tuple()
			for E in I:D=D+tuple(E for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		F,G=val_func_ulcorner(A);J,K=-F,-G;L=val_func_shift(A,(J,K));H=set()
		for(E,(M,N))in L:
			for O in range(B):
				for P in range(B):H.add((E,(M*B+O,N*B+P)))
		return val_func_shift(frozenset(H),(F,G))
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def mval_func_apply(A,B):return val_func_merge(val_func_apply(A,B))
def val_func_fork(A,B,C):return lambda D:A(B(D),C(D))
def val_func_lbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(B,D)
	elif C==3:return lambda D,E:A(B,D,E)
	else:return lambda D,E,F:A(B,D,E,F)
def val_func_rbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(D,B)
	elif C==3:return lambda D,E:A(D,E,B)
	else:return lambda D,E,F:A(D,E,F,B)
def val_func_matcher(A,B):return lambda C:A(C)==B
def val_func_chain(A,B,C):return lambda D:A(B(C(D)))
def val_func_astuple(A,B):return A,B
def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_both(A,B):return A and B
def val_func_initset(A):return frozenset({A})
def val_func_size(A):return len(A)
def val_func_difference(A,B):return type(A)(A for A in A if A not in B)
def val_func_flip(A):return not A
def val_func_add(A,B):
	if isinstance(A,int)and isinstance(B,int):return A+B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]+B[0],A[1]+B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A+B[0],A+B[1]
	return A[0]+B,A[1]+B
def p(A):A=tuple(map(tuple,A));B=val_func_ofcolor(A,0);E=val_func_astuple(0,(0,0));F=val_func_initset(E);G=val_func_upscale(F,3);H=val_func_toindices(G);C=val_func_lbind(val_func_shift,H);I=val_func_rbind(val_func_difference,B);J=val_func_chain(val_func_size,I,C);D=val_func_matcher(J,0);K=val_func_lbind(val_func_add,(-1,-1));L=val_func_chain(val_func_flip,D,K);M=val_func_fork(val_func_both,D,L);N=val_func_sfilter(B,M);O=mval_func_apply(C,N);P=val_func_fill(A,1,O);return[*map(list,P)]