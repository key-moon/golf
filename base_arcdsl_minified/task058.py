def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_shift(patch,directions):
	A=patch
	if len(A)==0:return A
	B,C=directions
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(D+B,E+C))for(A,(D,E))in A)
	return frozenset((A+B,D+C)for(A,D)in A)
def val_func_ulcorner(patch):return tuple(map(min,zip(*val_func_toindices(patch))))
def val_func_canvas(value,dimensions):A=dimensions;return tuple(tuple(value for A in range(A[1]))for B in range(A[0]))
def val_func_vconcat(a,b):return a+b
def val_func_hconcat(a,b):return tuple(A+B for(A,B)in zip(a,b))
def val_func_upscale(element,factor):
	B=element;A=factor
	if isinstance(B,tuple):
		C=tuple()
		for I in B:
			D=tuple()
			for E in I:D=D+tuple(E for A in range(A))
			C=C+tuple(D for A in range(A))
		return C
	else:
		if len(B)==0:return frozenset()
		F,G=val_func_ulcorner(B);J,K=-F,-G;L=val_func_shift(B,(J,K));H=set()
		for(E,(M,N))in L:
			for O in range(A):
				for P in range(A):H.add((E,(M*A+O,N*A+P)))
		return val_func_shift(frozenset(H),(F,G))
def val_func_vval_func_upscale(grid,factor):
	A=tuple()
	for B in grid:A=A+tuple(B for A in range(factor))
	return A
def val_func_hval_func_upscale(grid,factor):
	A=tuple()
	for C in grid:
		B=tuple()
		for D in C:B=B+tuple(D for A in range(factor))
		A=A+(B,)
	return A
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_rot90(grid):return tuple(A for A in zip(*grid[::-1]))
def val_func_width(piece):
	A=piece
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_height(piece):
	A=piece
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def val_func_fork(outer,a,b):return lambda x:outer(a(x),b(x))
def val_func_power(function,n):
	A=function
	if n==1:return A
	return val_func_compose(A,val_func_power(A,n-1))
def val_func_lbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def val_func_rbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def val_func_chain(h,g,f):return lambda x:h(g(f(x)))
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_branch(condition,a,b):return a if condition else b
def val_func_astuple(a,b):return a,b
def val_func_insert(value,container):return container.union(frozenset({value}))
def val_func_decrement(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def val_func_initset(value):return frozenset({value})
def val_func_even(n):return n%2==0
def val_func_subtract(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):I=tuple(map(tuple,I));B=val_func_width(I);D=val_func_astuple(1,2);E=val_func_astuple(2,2);F=val_func_astuple(2,1);G=val_func_astuple(3,1);A=val_func_canvas(3,(1,1));H=val_func_upscale(A,4);J=val_func_initset((1,0));C=val_func_insert((1,1),J);K=val_func_insert(D,C);L=val_func_insert(E,K);M=val_func_fill(H,0,L);N=val_func_vval_func_upscale(A,5);O=val_func_hval_func_upscale(N,3);P=val_func_insert(F,C);Q=val_func_insert(G,P);R=val_func_fill(O,0,Q);S=val_func_even(B);T=val_func_branch(S,M,R);U=val_func_canvas(0,(1,1));V=val_func_lbind(val_func_hval_func_upscale,U);W=val_func_chain(V,val_func_decrement,val_func_height);X=val_func_rbind(val_func_hconcat,A);Y=val_func_compose(X,W);Z=val_func_lbind(val_func_hval_func_upscale,A);a=val_func_compose(Z,val_func_height);b=val_func_fork(val_func_vconcat,Y,val_func_rot90);c=val_func_fork(val_func_vconcat,a,b);d=val_func_subtract(B,4);e=val_func_power(c,d);f=e(T);return[*map(list,f)]