def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_height(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def val_func_llcorner(A):return tuple(map(lambda B:{0:max,1:min}[B[0]](B[1]),enumerate(zip(*val_func_toindices(A)))))
def val_func_urcorner(A):return tuple(map(lambda B:{0:min,1:max}[B[0]](B[1]),enumerate(zip(*val_func_toindices(A)))))
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_lrcorner(A):return tuple(map(max,zip(*val_func_toindices(A))))
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_box(A):
	if len(A)==0:return A
	F,G=val_func_ulcorner(A);H,I=val_func_lrcorner(A);B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def val_func_corners(A):return frozenset({val_func_ulcorner(A),val_func_urcorner(A),val_func_llcorner(A),val_func_lrcorner(A)})
def val_func_canvas(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def val_func_paint(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def val_func_asobject(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def val_func_manhattan(A,B):return min(abs(A-D)+abs(C-E)for(A,C)in val_func_toindices(A)for(D,E)in val_func_toindices(B))
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def val_func_shape(A):return val_func_height(A),val_func_width(A)
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_fork(A,B,C):return lambda D:A(B(D),C(D))
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
def val_func_chain(A,B,C):return lambda D:A(B(C(D)))
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_astuple(A,B):return A,B
def val_func_first(A):return next(iter(A))
def val_func_initset(A):return frozenset({A})
def val_func_argmin(A,B):return min(A,key=B)
def val_func_difference(A,B):return type(A)(A for A in A if A not in B)
def val_func_add(A,B):
	if isinstance(A,int)and isinstance(B,int):return A+B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]+B[0],A[1]+B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A+B[0],A+B[1]
	return A[0]+B,A[1]+B
def val_func_identity(A):return A
def p(A):A=tuple(map(tuple,A));D=val_func_shape(A);E=val_func_add(D,2);B=val_func_canvas(0,E);F=val_func_asobject(A);C=val_func_shift(F,(1,1));G=val_func_paint(B,C);H=val_func_asindices(B);I=val_func_fork(val_func_difference,val_func_box,val_func_corners);J=I(H);K=val_func_lbind(val_func_lbind,val_func_manhattan);L=val_func_rbind(val_func_compose,val_func_initset);M=val_func_chain(L,K,val_func_initset);N=val_func_lbind(val_func_argmin,C);O=val_func_chain(val_func_first,N,M);P=val_func_fork(val_func_astuple,O,val_func_identity);Q=val_func_apply(P,J);R=val_func_paint(G,Q);return[*map(list,R)]