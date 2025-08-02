def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
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
def val_func_mostcolor(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_connect(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def val_func_shoot(start,direction):B=direction;A=start;return val_func_connect(A,(A[0]+42*B[0],A[1]+42*B[1]))
def underval_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);G=val_func_mostcolor(A);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:
			if B[C][D]==G:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def mval_func_apply(function,container):return val_func_merge(val_func_apply(function,container))
def val_func_fork(outer,a,b):return lambda x:outer(a(x),b(x))
def val_func_lbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def val_func_matcher(function,target):return lambda x:function(x)==target
def val_func_chain(h,g,f):return lambda x:h(g(f(x)))
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_first(container):return next(iter(container))
def val_func_sfilter(container,condition):A=container;return type(A)(A for A in A if condition(A))
def val_func_toivec(i):return i,0
def val_func_decrement(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def val_func_greater(a,b):return a>b
def val_func_double(n):return n*2 if isinstance(n,int)else(n[0]*2,n[1]*2)
def val_func_invert(n):return-n if isinstance(n,int)else(-n[0],-n[1])
def val_func_identity(x):return x
def p(I):I=tuple(map(tuple,I));C=val_func_ofcolor(I,1);D=val_func_ofcolor(I,2);E=val_func_ofcolor(I,5);F=val_func_uppermost(E);B=val_func_chain(val_func_toivec,val_func_decrement,val_func_double);G=val_func_lbind(val_func_greater,F);A=val_func_compose(G,val_func_first);H=val_func_chain(val_func_invert,B,A);J=val_func_fork(val_func_shoot,val_func_identity,H);K=val_func_compose(B,A);L=val_func_fork(val_func_shoot,val_func_identity,K);M=val_func_lbind(val_func_matcher,A);N=val_func_compose(M,A);O=val_func_fork(val_func_sfilter,L,N);P=mval_func_apply(J,C);Q=mval_func_apply(O,D);R=underval_func_fill(I,2,Q);S=val_func_fill(R,1,P);return[*map(list,S)]