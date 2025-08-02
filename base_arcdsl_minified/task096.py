def val_func_pval_func_apply(function,a,b):return tuple(function(A,B)for(A,B)in zip(a,b))
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
def ival_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(loc):return val_func_dval_func_neighbors(loc)|ival_func_neighbors(loc)
def val_func_dval_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
def val_func_palette(element):
	A=element
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_lrcorner(patch):return tuple(map(max,zip(*val_func_toindices(patch))))
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
def val_func_canvas(value,dimensions):A=dimensions;return tuple(tuple(value for A in range(A[1]))for B in range(A[0]))
def val_func_paint(grid,obj):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(G,(C,D))in obj:
		if 0<=C<E and 0<=D<F:B[C][D]=G
	return tuple(tuple(A)for A in B)
def val_func_cmirror(piece):
	A=piece
	if isinstance(A,tuple):return tuple(zip(*(A[::-1]for A in A[::-1])))
	return val_func_vmirror(val_func_dmirror(val_func_vmirror(A)))
def val_func_dmirror(piece):
	A=piece
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_vmirror(piece):
	A=piece
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=val_func_ulcorner(A)[1]+val_func_lrcorner(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def val_func_hmirror(piece):
	A=piece
	if isinstance(A,tuple):return A[::-1]
	B=val_func_ulcorner(A)[0]+val_func_lrcorner(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def val_func_rot90(grid):return tuple(A for A in zip(*grid[::-1]))
def val_func_color(obj):return next(iter(obj))[0]
def val_func_centerofmass(patch):A=patch;return tuple(map(lambda x:sum(x)//len(A),zip(*val_func_toindices(A))))
def val_func_manhattan(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in val_func_toindices(a)for(C,D)in val_func_toindices(b))
def val_func_fgpartition(grid):A=grid;return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in val_func_palette(A)-{val_func_mostval_func_color(A)})
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
def val_func_normalize(patch):
	A=patch
	if len(A)==0:return A
	return val_func_shift(A,(-val_func_uppermost(A),-val_func_leftmost(A)))
def val_func_shift(patch,directions):
	A=patch
	if len(A)==0:return A
	B,C=directions
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(D+B,E+C))for(A,(D,E))in A)
	return frozenset((A+B,D+C)for(A,D)in A)
def val_func_val_func_colorfilter(objs,value):return frozenset(A for A in objs if next(iter(A))[0]==value)
def val_func_width(piece):
	A=piece
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_mostval_func_color(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_prval_func_apply(function,a,b):return frozenset(function(B,A)for A in b for B in a)
def val_func_mval_func_pval_func_apply(function,a,b):return val_func_merge(val_func_pval_func_apply(function,a,b))
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
def val_func_branch(condition,a,b):return a if condition else b
def val_func_pair(a,b):return tuple(zip(a,b))
def val_func_astuple(a,b):return a,b
def val_func_interval(start,stop,step):return tuple(range(start,stop,step))
def val_func_remove(value,container):A=container;return type(A)(A for A in A if A!=value)
def val_func_insert(value,container):return container.union(frozenset({value}))
def val_func_positive(x):return x>0
def val_func_decrement(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def val_func_increment(x):return x+1 if isinstance(x,int)else(x[0]+1,x[1]+1)
def val_func_initset(value):return frozenset({value})
def val_func_argmin(container,compfunc):return min(container,key=compfunc)
def val_func_valmax(container,compfunc):A=compfunc;return A(max(container,key=A,default=0))
def val_func_minimum(container):return min(container,default=0)
def val_func_size(container):return len(container)
def val_func_order(container,compfunc):return tuple(sorted(container,key=compfunc))
def val_func_contained(value,container):return value in container
def val_func_double(n):return n*2 if isinstance(n,int)else(n[0]*2,n[1]*2)
def val_func_invert(n):return-n if isinstance(n,int)else(-n[0],-n[1])
def val_func_add(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def val_func_identity(x):return x
def p(I):I=tuple(map(tuple,I));G=val_func_mostval_func_color(I);B=val_func_fgpartition(I);H=val_func_objects(I,True,False,True);J=val_func_rbind(val_func_valmax,val_func_width);K=val_func_lbind(val_func_val_func_colorfilter,H);L=val_func_compose(K,val_func_color);M=val_func_compose(val_func_double,J);N=val_func_lbind(val_func_prval_func_apply,val_func_manhattan);O=val_func_fork(N,val_func_identity,val_func_identity);P=val_func_lbind(val_func_remove,0);Q=val_func_compose(P,O);R=val_func_rbind(val_func_branch,-2);S=val_func_fork(R,val_func_positive,val_func_decrement);T=val_func_chain(S,val_func_minimum,Q);U=val_func_fork(val_func_add,T,M);V=val_func_compose(U,L);W=val_func_compose(val_func_invert,V);X=val_func_order(B,W);Y=val_func_rbind(val_func_argmin,val_func_centerofmass);Z=val_func_compose(val_func_initset,val_func_vmirror);a=val_func_fork(val_func_insert,val_func_dmirror,Z);b=val_func_fork(val_func_insert,val_func_cmirror,a);c=val_func_fork(val_func_insert,val_func_hmirror,b);d=val_func_compose(Y,c);e=val_func_apply(d,X);C=val_func_size(B);f=val_func_apply(val_func_size,B);g=val_func_contained(1,f);h=val_func_increment(C);D=val_func_branch(g,C,h);i=val_func_double(D);E=val_func_decrement(i);j=val_func_apply(val_func_normalize,e);F=val_func_interval(0,D,1);k=val_func_pair(F,F);A=val_func_mval_func_pval_func_apply(val_func_shift,j,k);l=val_func_astuple(E,E);m=val_func_canvas(G,l);n=val_func_paint(m,A);o=val_func_rot90(n);p=val_func_paint(o,A);q=val_func_rot90(p);r=val_func_paint(q,A);s=val_func_rot90(r);t=val_func_paint(s,A);return[*map(list,t)]