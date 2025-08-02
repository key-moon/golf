def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_paint(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def val_func_dmirror(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_toobject(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in val_func_toindices(A)if 0<=A<D and 0<=C<E)
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def pval_func_apply(A,B,C):return tuple(A(B,C)for(B,C)in zip(B,C))
def mval_func_apply(A,B):return val_func_merge(val_func_apply(A,B))
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_lbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(B,D)
	elif C==3:return lambda D,E:A(B,D,E)
	else:return lambda D,E,F:A(B,D,E,F)
def val_func_pair(A,B):return tuple(zip(A,B))
def val_func_interval(A,B,C):return tuple(range(A,B,C))
def val_func_maximum(A):return max(A,default=0)
def val_func_difference(A,B):return type(A)(A for A in A if A not in B)
def val_func_invert(A):return-A if isinstance(A,int)else(-A[0],-A[1])
def p(A):A=tuple(map(tuple,A));D=val_func_asindices(A);E=val_func_dmirror(A);C=val_func_invert(9);F=pval_func_apply(val_func_pair,A,E);G=val_func_lbind(val_func_apply,val_func_maximum);B=val_func_apply(G,F);H=val_func_ofcolor(B,0);I=val_func_difference(D,H);J=val_func_toobject(I,B);K=val_func_interval(C,9,1);L=val_func_interval(9,C,-1);M=val_func_pair(K,L);N=val_func_lbind(val_func_shift,J);O=mval_func_apply(N,M);P=val_func_paint(B,O);return[*map(list,P)]