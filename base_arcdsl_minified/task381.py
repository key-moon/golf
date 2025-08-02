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
def val_func_trim(A):return tuple(A[1:-1]for A in A[1:-1])
def val_func_connect(A,B):
	C,D=A;E,F=B;G=min(C,E);H=max(C,E)+1;I=min(D,F);J=max(D,F)+1
	if C==E:return frozenset((C,A)for A in range(I,J))
	elif D==F:return frozenset((A,D)for A in range(G,H))
	elif E-C==F-D:return frozenset((A,B)for(A,B)in zip(range(G,H),range(I,J)))
	elif E-C==D-F:return frozenset((A,B)for(A,B)in zip(range(G,H),range(J-1,I-1,-1)))
	return frozenset()
def val_func_paint(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_asobject(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def mval_func_apply(A,B):return val_func_merge(val_func_apply(A,B))
def val_func_fork(A,B,C):return lambda D:A(B(D),C(D))
def val_func_power(A,B):
	if B==1:return A
	return val_func_compose(A,val_func_power(A,B-1))
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_product(A,B):return frozenset((C,B)for B in B for C in A)
def val_func_last(A):return max(enumerate(A))[1]
def val_func_first(A):return next(iter(A))
def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_intersection(A,B):return A&B
def val_func_equality(A,B):return A==B
def p(A):A=tuple(map(tuple,A));B=val_func_ofcolor(A,2);C=val_func_ofcolor(A,0);D=val_func_product(B,B);E=val_func_power(val_func_first,2);F=val_func_compose(val_func_first,val_func_last);G=val_func_fork(val_func_equality,E,F);H=val_func_sfilter(D,G);I=val_func_fork(val_func_connect,val_func_first,val_func_last);J=mval_func_apply(I,H);K=val_func_intersection(J,C);L=val_func_fill(A,9,K);M=val_func_trim(L);N=val_func_asobject(M);O=val_func_shift(N,(1,1));P=val_func_paint(A,O);return[*map(list,P)]