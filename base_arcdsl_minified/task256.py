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
def val_func_mostcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_connect(A,B):
	C,D=A;E,F=B;G=min(C,E);H=max(C,E)+1;I=min(D,F);J=max(D,F)+1
	if C==E:return frozenset((C,A)for A in range(I,J))
	elif D==F:return frozenset((A,D)for A in range(G,H))
	elif E-C==F-D:return frozenset((A,B)for(A,B)in zip(range(G,H),range(I,J)))
	elif E-C==D-F:return frozenset((A,B)for(A,B)in zip(range(G,H),range(J-1,I-1,-1)))
	return frozenset()
def val_func_shoot(A,B):return val_func_connect(A,(A[0]+42*B[0],A[1]+42*B[1]))
def val_func_underfill(A,B,C):
	G,H=len(A),len(A[0]);I=val_func_mostcolor(A);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_urcorner(A):return tuple(map(lambda B:{0:min,1:max}[B[0]](B[1]),enumerate(zip(*val_func_toindices(A)))))
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def mval_func_apply(A,B):return val_func_merge(val_func_apply(A,B))
def val_func_rbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(D,B)
	elif C==3:return lambda D,E:A(D,E,B)
	else:return lambda D,E,F:A(D,E,F,B)
def p(A):A=tuple(map(tuple,A));F=val_func_ofcolor(A,2);B=val_func_urcorner(F);C=val_func_shoot(B,(-1,1));D=val_func_shoot(B,(1,-1));G=val_func_underfill(A,3,C);H=val_func_underfill(G,1,D);E=val_func_rbind(val_func_shoot,(0,-1));I=mval_func_apply(E,C);J=mval_func_apply(E,D);K=val_func_underfill(H,1,J);L=val_func_underfill(K,3,I);return[*map(list,L)]