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
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_height(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def val_func_shape(A):return val_func_height(A),val_func_width(A)
def val_func_occurrences(A,B):
	C=set();K=val_func_normalize(B);D,E=len(A),len(A[0]);L,M=val_func_shape(B);N,O=D-L+1,E-M+1
	for F in range(N):
		for G in range(O):
			H=True
			for(P,(I,J))in val_func_shift(K,(F,G)):
				if not(0<=I<D and 0<=J<E and A[I][J]==P):H=False;break
			if H:C.add((F,G))
	return frozenset(C)
def val_func_paint(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def val_func_normalize(A):
	if len(A)==0:return A
	return val_func_shift(A,(-val_func_uppermost(A),-val_func_leftmost(A)))
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_recolor(A,B):return frozenset((A,B)for B in val_func_toindices(B))
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_apply(A,B):return type(B)(A(B)for B in B)
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
def val_func_chain(A,B,C):return lambda D:A(B(C(D)))
def val_func_astuple(A,B):return A,B
def val_func_insert(A,B):return B.union(frozenset({A}))
def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_initset(A):return frozenset({A})
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_contained(A,B):return A in B
def val_func_flip(A):return not A
def p(A):A=tuple(map(tuple,A));C=val_func_ofcolor(A,2);B=val_func_recolor(0,C);D=val_func_normalize(B);E=val_func_occurrences(A,B);F=val_func_lbind(val_func_shift,D);G=val_func_apply(F,E);H=val_func_astuple(1,3);I=val_func_astuple(5,1);J=val_func_astuple(2,6);K=val_func_initset(H);L=val_func_insert(I,K);M=val_func_insert(J,L);N=val_func_rbind(val_func_contained,M);O=val_func_chain(val_func_flip,N,val_func_ulcorner);P=val_func_sfilter(G,O);Q=val_func_merge(P);R=val_func_recolor(2,Q);S=val_func_paint(A,R);return[*map(list,S)]