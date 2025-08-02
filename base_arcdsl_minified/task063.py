def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_mostcolor(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_crop(grid,start,dims):A=start;return tuple(B[A[1]:A[1]+dims[1]]for B in grid[A[0]:A[0]+dims[0]])
def val_func_hfrontier(location):return frozenset((location[0],A)for A in range(30))
def val_func_vfrontier(location):return frozenset((A,location[1])for A in range(30))
def val_func_vsplit(grid,n):A=grid;B,D=len(A)//n,len(A[0]);E=len(A)%n!=0;return tuple(val_func_crop(A,(B*C+C*E,0),(B,D))for C in range(n))
def val_func_underfill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);G=val_func_mostcolor(A);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:
			if B[C][D]==G:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_rot90(grid):return tuple(A for A in zip(*grid[::-1]))
def val_func_colorcount(element,value):
	B=value;A=element
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def val_func_height(piece):
	A=piece
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def mval_func_apply(function,container):return val_func_merge(val_func_apply(function,container))
def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
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
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_pair(a,b):return tuple(zip(a,b))
def val_func_astuple(a,b):return a,b
def val_func_interval(start,stop,step):return tuple(range(start,stop,step))
def val_func_last(container):return max(enumerate(container))[1]
def val_func_first(container):return next(iter(container))
def val_func_sfilter(container,condition):A=container;return type(A)(A for A in A if condition(A))
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_subtract(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):I=tuple(map(tuple,I));A=val_func_height(I);D=val_func_rot90(I);E=val_func_subtract(A,2);B=val_func_interval(0,A,1);F=val_func_rbind(val_func_colorcount,0);G=val_func_matcher(F,E);H=val_func_rbind(val_func_vsplit,A);J=val_func_lbind(val_func_apply,G);C=val_func_compose(J,H);K=C(I);L=val_func_pair(B,K);M=val_func_sfilter(L,val_func_last);N=mval_func_apply(val_func_hfrontier,M);O=C(D);P=val_func_pair(O,B);Q=val_func_sfilter(P,val_func_first);R=mval_func_apply(val_func_vfrontier,Q);S=val_func_astuple(N,R);T=val_func_merge(S);U=val_func_underfill(I,3,T);return[*map(list,U)]