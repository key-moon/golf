def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
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
def val_func_palette(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_recolor(A,B):return frozenset((A,B)for B in val_func_toindices(B))
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def prval_func_apply(A,B,C):return frozenset(A(D,C)for C in C for D in B)
def mval_func_apply(A,B):return val_func_merge(val_func_apply(A,B))
def val_func_fork(A,B,C):return lambda D:A(B(D),C(D))
def val_func_lbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(B,D)
	elif C==3:return lambda D,E:A(B,D,E)
	else:return lambda D,E,F:A(B,D,E,F)
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_remove(A,B):return type(B)(B for B in B if B!=A)
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_identity(A):return A
def p(A):A=tuple(map(tuple,A));C=val_func_palette(A);D=val_func_remove(0,C);B=val_func_lbind(val_func_ofcolor,A);E=val_func_lbind(prval_func_apply,val_func_connect);F=val_func_fork(E,B,B);G=val_func_compose(val_func_merge,F);H=val_func_fork(val_func_recolor,val_func_identity,G);I=mval_func_apply(H,D);J=val_func_paint(A,I);return[*map(list,J)]