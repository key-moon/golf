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
def val_func_underfill(A,B,C):
	G,H=len(A),len(A[0]);I=val_func_mostcolor(A);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_astuple(A,B):return A,B
def val_func_minimum(A):return min(A,default=0)
def val_func_maximum(A):return max(A,default=0)
def val_func_combine(A,B):return type(A)((*A,*B))
def p(A):A=tuple(map(tuple,A));D=val_func_ofcolor(A,2);E=val_func_ofcolor(A,3);B=val_func_uppermost(D);H=val_func_leftmost(D);I=val_func_uppermost(E);C=val_func_leftmost(E);F=val_func_astuple(B,I);J=val_func_minimum(F);K=val_func_maximum(F);L=val_func_astuple(J,C);M=val_func_astuple(K,C);N=val_func_connect(L,M);G=val_func_astuple(H,C);O=val_func_minimum(G);P=val_func_maximum(G);Q=val_func_astuple(B,O);R=val_func_astuple(B,P);S=val_func_connect(Q,R);T=val_func_combine(N,S);U=val_func_underfill(A,8,T);return[*map(list,U)]