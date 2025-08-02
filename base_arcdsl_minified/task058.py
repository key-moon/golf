def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_canvas(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def val_func_vconcat(A,B):return A+B
def val_func_hconcat(A,B):return tuple(A+B for(A,B)in zip(A,B))
def val_func_upscale(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for I in A:
			D=tuple()
			for E in I:D=D+tuple(E for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		F,G=val_func_ulcorner(A);J,K=-F,-G;L=val_func_shift(A,(J,K));H=set()
		for(E,(M,N))in L:
			for O in range(B):
				for P in range(B):H.add((E,(M*B+O,N*B+P)))
		return val_func_shift(frozenset(H),(F,G))
def vval_func_upscale(A,B):
	C=tuple()
	for D in A:C=C+tuple(D for A in range(B))
	return C
def hval_func_upscale(A,B):
	C=tuple()
	for E in A:
		D=tuple()
		for F in E:D=D+tuple(F for A in range(B))
		C=C+(D,)
	return C
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_rot90(A):return tuple(A for A in zip(*A[::-1]))
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_height(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def val_func_fork(A,B,C):return lambda D:A(B(D),C(D))
def val_func_power(A,B):
	if B==1:return A
	return val_func_compose(A,val_func_power(A,B-1))
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
def val_func_branch(A,B,C):return B if A else C
def val_func_astuple(A,B):return A,B
def val_func_insert(A,B):return B.union(frozenset({A}))
def val_func_decrement(A):return A-1 if isinstance(A,int)else(A[0]-1,A[1]-1)
def val_func_initset(A):return frozenset({A})
def val_func_even(A):return A%2==0
def val_func_subtract(A,B):
	if isinstance(A,int)and isinstance(B,int):return A-B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]-B[0],A[1]-B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A-B[0],A-B[1]
	return A[0]-B,A[1]-B
def p(A):A=tuple(map(tuple,A));C=val_func_width(A);E=val_func_astuple(1,2);F=val_func_astuple(2,2);G=val_func_astuple(2,1);H=val_func_astuple(3,1);B=val_func_canvas(3,(1,1));I=val_func_upscale(B,4);J=val_func_initset((1,0));D=val_func_insert((1,1),J);K=val_func_insert(E,D);L=val_func_insert(F,K);M=val_func_fill(I,0,L);N=vval_func_upscale(B,5);O=hval_func_upscale(N,3);P=val_func_insert(G,D);Q=val_func_insert(H,P);R=val_func_fill(O,0,Q);S=val_func_even(C);T=val_func_branch(S,M,R);U=val_func_canvas(0,(1,1));V=val_func_lbind(hval_func_upscale,U);W=val_func_chain(V,val_func_decrement,val_func_height);X=val_func_rbind(val_func_hconcat,B);Y=val_func_compose(X,W);Z=val_func_lbind(hval_func_upscale,B);a=val_func_compose(Z,val_func_height);b=val_func_fork(val_func_vconcat,Y,val_func_rot90);c=val_func_fork(val_func_vconcat,a,b);d=val_func_subtract(C,4);e=val_func_power(c,d);f=e(T);return[*map(list,f)]