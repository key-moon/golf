def val_func_sfilter(container,condition):A=container;return type(A)(A for A in A if condition(A))
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_toobject(patch,grid):A=grid;D,E=len(A),len(A[0]);return frozenset((A[B][C],(B,C))for(B,C)in val_func_toindices(patch)if 0<=B<D and 0<=C<E)
def val_func_colorcount(element,value):
	B=value;A=element
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def val_func_leastcolor(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_fork(outer,a,b):return lambda x:outer(a(x),b(x))
def val_func_rbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def val_func_matcher(function,target):return lambda x:function(x)==target
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_product(a,b):return frozenset((B,A)for A in b for B in a)
def val_func_interval(start,stop,step):return tuple(range(start,stop,step))
def val_func_last(container):return max(enumerate(container))[1]
def val_func_first(container):return next(iter(container))
def val_func_mfilter(container,function):return val_func_merge(val_func_sfilter(container,function))
def val_func_valmax(container,compfunc):A=compfunc;return A(max(container,key=A,default=0))
def val_func_flip(b):return not b
def val_func_add(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def val_func_identity(x):return x
def p(I):I=tuple(map(tuple,I));B=val_func_leastcolor(I);C=val_func_interval(0,9,4);G=val_func_product(C,C);H=val_func_rbind(val_func_add,3);J=val_func_rbind(val_func_interval,1);D=val_func_fork(J,val_func_identity,H);K=val_func_compose(D,val_func_first);L=val_func_compose(D,val_func_last);M=val_func_fork(val_func_product,K,L);N=val_func_rbind(val_func_colorcount,B);O=val_func_rbind(val_func_toobject,I);E=val_func_compose(N,O);A=val_func_apply(M,G);P=val_func_valmax(A,E);F=val_func_matcher(E,P);Q=val_func_compose(val_func_flip,F);R=val_func_mfilter(A,F);S=val_func_mfilter(A,Q);T=val_func_fill(I,B,R);U=val_func_fill(T,0,S);return[*map(list,U)]