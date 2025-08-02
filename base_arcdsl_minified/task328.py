def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def ival_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(loc):return val_func_dval_func_neighbors(loc)|ival_func_neighbors(loc)
def val_func_dval_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_mostval_func_color(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
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
def val_func_center(patch):A=patch;return val_func_uppermost(A)+val_func_height(A)//2,val_func_leftmost(A)+val_func_width(A)//2
def val_func_paint(grid,obj):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(G,(C,D))in obj:
		if 0<=C<E and 0<=D<F:B[C][D]=G
	return tuple(tuple(A)for A in B)
def val_func_color(obj):return next(iter(obj))[0]
def val_func_objects(grid,univalued,diagonal,without_bg):
	A=grid;H=val_func_mostval_func_color(A)if without_bg else None;I=set();D=set();L,M=len(A),len(A[0]);N=val_func_asindices(A);O=val_func_neighbors if diagonal else val_func_dval_func_neighbors
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
def val_func_reval_func_color(value,patch):return frozenset((value,A)for A in val_func_toindices(patch))
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
def mval_func_apply(function,container):return val_func_merge(val_func_apply(function,container))
def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
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
def val_func_astuple(a,b):return a,b
def val_func_remove(value,container):A=container;return type(A)(A for A in A if A!=value)
def val_func_last(container):return max(enumerate(container))[1]
def val_func_first(container):return next(iter(container))
def val_func_sfilter(container,condition):A=container;return type(A)(A for A in A if condition(A))
def val_func_sign(x):
	if isinstance(x,int):return 0 if x==0 else 1 if x>0 else-1
	return 0 if x[0]==0 else 1 if x[0]>0 else-1,0 if x[1]==0 else 1 if x[1]>0 else-1
def val_func_argmin(container,compfunc):return min(container,key=compfunc)
def val_func_valmin(container,compfunc):A=compfunc;return A(min(container,key=A,default=0))
def val_func_maximum(container):return max(container,default=0)
def val_func_greater(a,b):return a>b
def val_func_intersection(a,b):return a&b
def val_func_equality(a,b):return a==b
def val_func_even(n):return n%2==0
def val_func_multiply(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
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
def p(I):I=tuple(map(tuple,I));H=val_func_asindices(I);A=val_func_objects(I,True,False,True);J=val_func_fork(val_func_multiply,val_func_sign,val_func_identity);C=val_func_lbind(val_func_apply,J);K=val_func_chain(val_func_even,val_func_maximum,C);B=val_func_lbind(val_func_sfilter,H);L=val_func_fork(val_func_add,val_func_first,val_func_last);M=val_func_rbind(val_func_remove,A);N=val_func_compose(val_func_center,val_func_last);D=val_func_fork(val_func_subtract,val_func_first,N);O=val_func_compose(K,D);P=val_func_lbind(val_func_rbind,val_func_equality);Q=val_func_lbind(val_func_argmin,A);R=val_func_chain(L,C,D);S=val_func_lbind(val_func_lbind,val_func_astuple);E=val_func_lbind(val_func_rbind,val_func_astuple);T=val_func_lbind(val_func_compose,O);F=val_func_lbind(val_func_compose,R);G=val_func_compose(F,S);U=val_func_compose(F,E);V=val_func_compose(Q,G);W=val_func_rbind(val_func_compose,V);X=val_func_lbind(val_func_lbind,val_func_valmin);Y=val_func_rbind(val_func_compose,G);Z=val_func_chain(Y,X,M);a=val_func_lbind(val_func_fork,val_func_greater);b=val_func_fork(a,Z,U);c=val_func_chain(B,T,E);d=val_func_chain(B,W,P);e=val_func_fork(val_func_intersection,c,d);f=val_func_compose(B,b);g=val_func_fork(val_func_intersection,e,f);h=val_func_fork(val_func_reval_func_color,val_func_color,g);i=mval_func_apply(h,A);j=val_func_paint(I,i);return[*map(list,j)]