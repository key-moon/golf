def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_mostcolor(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_connect(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def val_func_underfill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);G=val_func_mostcolor(A);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:
			if B[C][D]==G:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def val_func_astuple(a,b):return a,b
def val_func_minimum(container):return min(container,default=0)
def val_func_maximum(container):return max(container,default=0)
def val_func_combine(a,b):return type(a)((*a,*b))
def p(I):I=tuple(map(tuple,I));C=val_func_ofcolor(I,2);D=val_func_ofcolor(I,3);A=val_func_uppermost(C);G=val_func_leftmost(C);H=val_func_uppermost(D);B=val_func_leftmost(D);E=val_func_astuple(A,H);J=val_func_minimum(E);K=val_func_maximum(E);L=val_func_astuple(J,B);M=val_func_astuple(K,B);N=val_func_connect(L,M);F=val_func_astuple(G,B);O=val_func_minimum(F);P=val_func_maximum(F);Q=val_func_astuple(A,O);R=val_func_astuple(A,P);S=val_func_connect(Q,R);T=val_func_combine(N,S);U=val_func_underfill(I,8,T);return[*map(list,U)]