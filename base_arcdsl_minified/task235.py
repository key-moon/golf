def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_crop(grid,start,dims):A=start;return tuple(B[A[1]:A[1]+dims[1]]for B in grid[A[0]:A[0]+dims[0]])
def val_func_canvas(value,dimensions):A=dimensions;return tuple(tuple(value for A in range(A[1]))for B in range(A[0]))
def val_func_hsplit(grid,n):A=grid;D,B=len(A),len(A[0])//n;E=len(A[0])%n!=0;return tuple(val_func_crop(A,(0,B*C+C*E),(D,B))for C in range(n))
def val_func_hupscale(grid,factor):
	A=tuple()
	for C in grid:
		B=tuple()
		for D in C:B=B+tuple(D for A in range(factor))
		A=A+(B,)
	return A
def val_func_ulcorner(patch):return tuple(map(min,zip(*val_func_toindices(patch))))
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_fork(outer,a,b):return lambda x:outer(a(x),b(x))
def val_func_power(function,n):
	A=function
	if n==1:return A
	return val_func_compose(A,val_func_power(A,n-1))
def val_func_rbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def val_func_matcher(function,target):return lambda x:function(x)==target
def val_func_chain(h,g,f):return lambda x:h(g(f(x)))
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_astuple(a,b):return a,b
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_size(container):return len(container)
def val_func_double(n):return n*2 if isinstance(n,int)else(n[0]*2,n[1]*2)
def val_func_multiply(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def val_func_add(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):I=tuple(map(tuple,I));D=val_func_hsplit(I,3);E=val_func_astuple(2,1);B=val_func_rbind(val_func_ofcolor,0);A=val_func_compose(val_func_ulcorner,B);F=val_func_compose(val_func_size,B);G=val_func_matcher(F,0);H=val_func_matcher(A,(1,1));J=val_func_matcher(A,(1,0));K=val_func_matcher(A,E);L=val_func_rbind(val_func_multiply,3);C=val_func_power(val_func_double,2);M=val_func_compose(val_func_double,G);N=val_func_chain(C,val_func_double,H);O=val_func_compose(L,J);P=val_func_compose(C,K);Q=val_func_fork(val_func_add,M,N);R=val_func_fork(val_func_add,O,P);S=val_func_fork(val_func_add,Q,R);T=val_func_rbind(val_func_canvas,(1,1));U=val_func_compose(T,S);V=val_func_apply(U,D);W=val_func_merge(V);X=val_func_hupscale(W,3);return[*map(list,X)]