def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_dmirror(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_compress(A):B=tuple(A for(A,B)in enumerate(A)if len(set(B))==1);C=tuple(A for(A,B)in enumerate(val_func_dmirror(A))if len(set(B))==1);return tuple(tuple(B for(A,B)in enumerate(D)if A not in C)for(A,D)in enumerate(A)if A not in B)
def val_func_canvas(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def val_func_palette(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_crop(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def val_func_colorcount(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
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
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_astuple(A,B):return A,B
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_order(A,B):return tuple(sorted(A,key=B))
def val_func_invert(A):return-A if isinstance(A,int)else(-A[0],-A[1])
def p(A):A=tuple(map(tuple,A));B=val_func_compress(A);C=val_func_astuple(3,1);D=val_func_palette(B);E=val_func_lbind(val_func_colorcount,B);F=val_func_compose(val_func_invert,E);G=val_func_order(D,F);H=val_func_rbind(val_func_canvas,(1,1));I=val_func_apply(H,G);J=val_func_merge(I);K=val_func_crop(J,(1,0),C);return[*map(list,K)]