def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
def val_func_height(piece):
	A=piece
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def val_func_palette(element):
	A=element
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_mostval_func_color(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_ulcorner(patch):return tuple(map(min,zip(*val_func_toindices(patch))))
def val_func_vfrontier(location):return frozenset((A,location[1])for A in range(30))
def val_func_paint(grid,obj):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(G,(C,D))in obj:
		if 0<=C<E and 0<=D<F:B[C][D]=G
	return tuple(tuple(A)for A in B)
def val_func_dmirror(piece):
	A=piece
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_color(obj):return next(iter(obj))[0]
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
def val_func_fgpartition(grid):A=grid;return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in val_func_palette(A)-{val_func_mostval_func_color(A)})
def val_func_reval_func_color(value,patch):return frozenset((value,A)for A in val_func_toindices(patch))
def val_func_portrait(piece):A=piece;return val_func_height(A)>val_func_width(A)
def val_func_width(piece):
	A=piece
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
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
def val_func_chain(h,g,f):return lambda x:h(g(f(x)))
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_branch(condition,a,b):return a if condition else b
def val_func_interval(start,stop,step):return tuple(range(start,stop,step))
def val_func_tojvec(j):return 0,j
def val_func_decrement(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_double(n):return n*2 if isinstance(n,int)else(n[0]*2,n[1]*2)
def val_func_identity(x):return x
def p(I):I=tuple(map(tuple,I));D=val_func_portrait(I);B=val_func_branch(D,val_func_dmirror,val_func_identity);A=B(I);C=val_func_fgpartition(A);E=val_func_merge(C);F=val_func_chain(val_func_double,val_func_decrement,val_func_width);G=F(E);H=val_func_compose(val_func_vfrontier,val_func_tojvec);J=val_func_lbind(mval_func_apply,H);K=val_func_rbind(val_func_interval,G);L=val_func_width(A);M=val_func_rbind(K,L);N=val_func_chain(J,M,val_func_leftmost);O=val_func_fork(val_func_reval_func_color,val_func_color,N);P=mval_func_apply(O,C);Q=val_func_paint(A,P);R=B(Q);return[*map(list,R)]