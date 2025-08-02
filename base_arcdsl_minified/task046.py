def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def ival_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(loc):return val_func_dval_func_neighbors(loc)|ival_func_neighbors(loc)
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
def val_func_mostcolor(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_canvas(value,dimensions):A=dimensions;return tuple(tuple(value for A in range(A[1]))for B in range(A[0]))
def val_func_paint(grid,obj):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(G,(C,D))in obj:
		if 0<=C<E and 0<=D<F:B[C][D]=G
	return tuple(tuple(A)for A in B)
def val_func_palette(element):
	A=element
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
def val_func_objects(grid,univalued,diagonal,without_bg):
	A=grid;H=val_func_mostcolor(A)if without_bg else None;I=set();D=set();L,M=len(A),len(A[0]);N=val_func_asindices(A);O=val_func_neighbors if diagonal else val_func_dval_func_neighbors
	for B in N:
		if B in D:continue
		E=A[B[0]][B[1]]
		if E==H:continue
		J={(E,B)};F={B}
		while len(F)>0:
			K=set()
			for C in F:
				G=A[C[0]][C[1]]
				if E==G if univalued else G!=H:J.add((G,C));D.add(C);K|={(A,B)for(A,B)in O(C)if 0<=A<L and 0<=B<M}
			F=K-D
		I.add(frozenset(J))
	return frozenset(I)
def val_func_dval_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_shift(patch,directions):
	A=patch
	if len(A)==0:return A
	B,C=directions
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(D+B,E+C))for(A,(D,E))in A)
	return frozenset((A+B,D+C)for(A,D)in A)
def val_func_recolor(value,patch):return frozenset((value,A)for A in val_func_toindices(patch))
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_width(piece):
	A=piece
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
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
def val_func_matcher(function,target):return lambda x:function(x)==target
def val_func_chain(h,g,f):return lambda x:h(g(f(x)))
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_astuple(a,b):return a,b
def val_func_other(container,value):return val_func_first(val_func_remove(value,container))
def val_func_remove(value,container):A=container;return type(A)(A for A in A if A!=value)
def val_func_last(container):return max(enumerate(container))[1]
def val_func_first(container):return next(iter(container))
def val_func_sfilter(container,condition):A=container;return type(A)(A for A in A if condition(A))
def val_func_decrement(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def val_func_initset(value):return frozenset({value})
def val_func_argmin(container,compfunc):return min(container,key=compfunc)
def val_func_size(container):return len(container)
def val_func_order(container,compfunc):return tuple(sorted(container,key=compfunc))
def val_func_intersection(a,b):return a&b
def val_func_combine(a,b):return type(a)((*a,*b))
def val_func_subtract(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def val_func_add(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def val_func_identity(x):return x
def p(I):F=False;I=tuple(map(tuple,I));A=val_func_objects(I,F,F,True);G=val_func_rbind(val_func_other,5);H=val_func_compose(G,val_func_palette);J=val_func_fork(val_func_recolor,H,val_func_identity);K=val_func_apply(J,A);L=val_func_order(K,val_func_leftmost);M=val_func_compose(val_func_last,val_func_last);B=val_func_lbind(val_func_matcher,M);N=val_func_compose(B,val_func_leftmost);O=val_func_compose(B,val_func_rightmost);P=val_func_fork(val_func_sfilter,val_func_identity,N);Q=val_func_fork(val_func_sfilter,val_func_identity,O);R=val_func_compose(val_func_dval_func_neighbors,val_func_last);S=val_func_rbind(val_func_chain,R);T=val_func_lbind(S,val_func_size);U=val_func_lbind(val_func_rbind,val_func_intersection);C=val_func_chain(T,U,val_func_toindices);V=val_func_fork(val_func_argmin,P,C);W=val_func_fork(val_func_argmin,Q,C);X=val_func_compose(val_func_last,V);Y=val_func_compose(val_func_last,W);Z=val_func_astuple(0,(1,-1));a=val_func_initset(Z);b=val_func_lbind(val_func_add,(0,1));c=val_func_chain(X,val_func_first,val_func_last);d=val_func_compose(Y,val_func_first);e=val_func_fork(val_func_subtract,d,c);D=val_func_compose(val_func_first,val_func_last);f=val_func_compose(b,e);g=val_func_fork(val_func_shift,D,f);h=val_func_fork(val_func_combine,val_func_first,g);i=val_func_fork(val_func_remove,D,val_func_last);j=val_func_fork(val_func_astuple,h,i);k=val_func_size(A);l=val_func_power(j,k);m=val_func_astuple(a,L);n=l(m);E=val_func_first(n);o=val_func_width(E);p=val_func_decrement(o);q=val_func_astuple(3,p);r=val_func_canvas(0,q);s=val_func_paint(r,E);return[*map(list,s)]