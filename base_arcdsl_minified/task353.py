def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_mostcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_cover(A,B):return val_func_fill(A,val_func_mostcolor(A),val_func_toindices(B))
def val_func_paint(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_move(A,B,C):return val_func_paint(val_func_cover(A,B),val_func_shift(B,C))
def val_func_recolor(A,B):return frozenset((A,B)for B in val_func_toindices(B))
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_first(A):return next(iter(A))
def val_func_sign(A):
	if isinstance(A,int):return 0 if A==0 else 1 if A>0 else-1
	return 0 if A[0]==0 else 1 if A[0]>0 else-1,0 if A[1]==0 else 1 if A[1]>0 else-1
def val_func_subtract(A,B):
	if isinstance(A,int)and isinstance(B,int):return A-B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]-B[0],A[1]-B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A-B[0],A-B[1]
	return A[0]-B,A[1]-B
def p(A):A=tuple(map(tuple,A));B=val_func_ofcolor(A,3);C=val_func_ofcolor(A,4);D=val_func_first(B);E=val_func_first(C);F=val_func_subtract(E,D);G=val_func_sign(F);H=val_func_recolor(3,B);I=val_func_move(A,H,G);return[*map(list,I)]