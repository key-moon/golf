def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_ulcorner(patch):return tuple(map(min,zip(*val_func_toindices(patch))))
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
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_shift(patch,directions):
	A=patch
	if len(A)==0:return A
	B,C=directions
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(D+B,E+C))for(A,(D,E))in A)
	return frozenset((A+B,D+C)for(A,D)in A)
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def mval_func_apply(function,container):return val_func_merge(val_func_apply(function,container))
def val_func_fork(outer,a,b):return lambda x:outer(a(x),b(x))
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
def val_func_matcher(function,target):return lambda x:function(x)==target
def val_func_chain(h,g,f):return lambda x:h(g(f(x)))
def val_func_astuple(a,b):return a,b
def val_func_sfilter(container,condition):A=container;return type(A)(A for A in A if condition(A))
def val_func_both(a,b):return a and b
def val_func_initset(value):return frozenset({value})
def val_func_size(container):return len(container)
def val_func_difference(a,b):return type(a)(A for A in a if A not in b)
def val_func_flip(b):return not b
def val_func_add(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):I=tuple(map(tuple,I));A=val_func_ofcolor(I,0);D=val_func_astuple(0,(0,0));E=val_func_initset(D);F=val_func_upscale(E,3);G=val_func_toindices(F);B=val_func_lbind(val_func_shift,G);H=val_func_rbind(val_func_difference,A);J=val_func_chain(val_func_size,H,B);C=val_func_matcher(J,0);K=val_func_lbind(val_func_add,(-1,-1));L=val_func_chain(val_func_flip,C,K);M=val_func_fork(val_func_both,C,L);N=val_func_sfilter(A,M);O=mval_func_apply(B,N);P=val_func_fill(I,1,O);return[*map(list,P)]