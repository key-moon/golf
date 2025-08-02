def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_ival_func_neighbors(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_dval_func_neighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_palette(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
def val_func_normalize(A):
	if len(A)==0:return A
	return val_func_shift(A,(-val_func_uppermost(A),-val_func_leftmost(A)))
def val_func_vperiod(A):
	B=val_func_normalize(A);D=val_func_height(B)
	for C in range(1,D):
		E=val_func_shift(B,(-C,0));F=frozenset({(B,(A,C))for(B,(A,C))in E if A>=0})
		if F.issubset(B):return C
def val_func_hperiod(A):
	B=val_func_normalize(A);C=val_func_width(B)
	for D in range(1,C):
		E=val_func_shift(B,(0,-D));F=frozenset({(B,(C,A))for(B,(C,A))in E if A>=0})
		if F.issubset(B):return D
	return C
def val_func_paint(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def val_func_asobject(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def val_func_partition(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in val_func_palette(A))
def val_func_neighbors(A):return val_func_dval_func_neighbors(A)|val_func_ival_func_neighbors(A)
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_crop(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def val_func_colorfilter(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_height(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def mval_func_apply(A,B):return val_func_merge(val_func_apply(A,B))
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_lbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(B,D)
	elif C==3:return lambda D,E:A(B,D,E)
	else:return lambda D,E,F:A(B,D,E,F)
def val_func_astuple(A,B):return A,B
def val_func_tojvec(A):return 0,A
def val_func_toivec(A):return A,0
def val_func_decrement(A):return A-1 if isinstance(A,int)else(A[0]-1,A[1]-1)
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_difference(A,B):return type(A)(A for A in A if A not in B)
def val_func_multiply(A,B):
	if isinstance(A,int)and isinstance(B,int):return A*B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]*B[0],A[1]*B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A*B[0],A*B[1]
	return A[0]*B,A[1]*B
def p(A):A=tuple(map(tuple,A));B=val_func_height(A);C=val_func_width(A);D=val_func_partition(A);E=val_func_colorfilter(D,0);F=val_func_difference(D,E);G=val_func_merge(F);H=val_func_astuple(B,1);I=val_func_astuple(1,C);J=val_func_decrement(B);K=val_func_decrement(C);L=val_func_toivec(K);M=val_func_tojvec(J);N=val_func_crop(A,L,I);O=val_func_crop(A,M,H);P=val_func_asobject(O);Q=val_func_asobject(N);R=val_func_vperiod(P);S=val_func_hperiod(Q);T=val_func_astuple(R,S);U=val_func_lbind(val_func_multiply,T);V=val_func_neighbors((0,0));W=mval_func_apply(val_func_neighbors,V);X=val_func_apply(U,W);Y=val_func_lbind(val_func_shift,G);Z=mval_func_apply(Y,X);a=val_func_paint(A,Z);return[*map(list,a)]