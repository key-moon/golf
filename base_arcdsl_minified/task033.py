def val_func_merge(A):return type(A)(B for A in A for B in A)
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
def val_func_underfill(A,B,C):
	G,H=len(A),len(A[0]);I=val_func_mostval_func_color(A);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_asobject(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def val_func_color(A):return next(iter(A))[0]
def val_func_palette(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_partition(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in val_func_palette(A))
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_crop(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def val_func_height(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def val_func_mostval_func_color(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def pval_func_apply(A,B,C):return tuple(A(B,C)for(B,C)in zip(B,C))
def mval_func_apply(A,B):return val_func_merge(val_func_apply(A,B))
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_lbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(B,D)
	elif C==3:return lambda D,E:A(B,D,E)
	else:return lambda D,E,F:A(B,D,E,F)
def val_func_matcher(A,B):return lambda C:A(C)==B
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_product(A,B):return frozenset((C,B)for B in B for C in A)
def val_func_astuple(A,B):return A,B
def val_func_interval(A,B,C):return tuple(range(A,B,C))
def val_func_last(A):return max(enumerate(A))[1]
def val_func_first(A):return next(iter(A))
def val_func_totuple(A):return tuple(A)
def val_func_extract(A,B):return next(A for A in A if B(A))
def val_func_initset(A):return frozenset({A})
def val_func_difference(A,B):return type(A)(A for A in A if A not in B)
def val_func_flip(A):return not A
def val_func_divide(A,B):
	if isinstance(A,int)and isinstance(B,int):return A//B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]//B[0],A[1]//B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A//B[0],A//B[1]
	return A[0]//B,A[1]//B
def val_func_multiply(A,B):
	if isinstance(A,int)and isinstance(B,int):return A*B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]*B[0],A[1]*B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A*B[0],A*B[1]
	return A[0]*B,A[1]*B
def val_func_subtract(A,B):
	if isinstance(A,int)and isinstance(B,int):return A-B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]-B[0],A[1]-B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A-B[0],A-B[1]
	return A[0]-B,A[1]-B
def val_func_add(A,B):
	if isinstance(A,int)and isinstance(B,int):return A+B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]+B[0],A[1]+B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A+B[0],A+B[1]
	return A[0]+B,A[1]+B
def p(A):A=tuple(map(tuple,A));I=val_func_height(A);J=val_func_mostval_func_color(A);K=val_func_asobject(A);L=val_func_subtract(I,2);B=val_func_divide(L,3);M=val_func_astuple(B,B);N=val_func_crop(A,(0,0),M);O=val_func_partition(N);P=val_func_matcher(val_func_color,0);Q=val_func_compose(val_func_flip,P);C=val_func_extract(O,Q);R=val_func_initset(J);S=val_func_palette(K);T=val_func_palette(C);U=val_func_difference(S,T);V=val_func_difference(U,R);W=val_func_first(V);D=val_func_interval(0,3,1);X=val_func_product(D,D);E=val_func_totuple(X);F=val_func_apply(val_func_first,E);G=val_func_apply(val_func_last,E);H=val_func_lbind(val_func_multiply,B);Y=val_func_apply(H,F);Z=val_func_apply(H,G);a=pval_func_apply(val_func_add,Y,F);b=pval_func_apply(val_func_add,Z,G);c=pval_func_apply(val_func_astuple,a,b);d=val_func_lbind(val_func_shift,C);e=mval_func_apply(d,c);f=val_func_underfill(A,W,e);return[*map(list,f)]