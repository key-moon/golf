def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def ival_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(loc):return val_func_dval_func_neighbors(loc)|ival_func_neighbors(loc)
def val_func_dval_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
def val_func_manhattan(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in val_func_toindices(a)for(C,D)in val_func_toindices(b))
def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
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
def val_func_lrcorner(patch):return tuple(map(max,zip(*val_func_toindices(patch))))
def val_func_ulcorner(patch):return tuple(map(min,zip(*val_func_toindices(patch))))
def val_func_backdrop(patch):
	A=patch
	if len(A)==0:return frozenset({})
	B=val_func_toindices(A);C,D=val_func_ulcorner(B);E,F=val_func_lrcorner(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def val_func_delta(patch):
	A=patch
	if len(A)==0:return frozenset({})
	return val_func_backdrop(A)-val_func_toindices(A)
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_position(a,b):
	A,B=val_func_center(val_func_toindices(a));C,D=val_func_center(val_func_toindices(b))
	if A==C:return 0,1 if B<D else-1
	elif B==D:return 1 if A<C else-1,0
	elif A<C:return 1,1 if B<D else-1
	elif A>C:return-1,1 if B<D else-1
def val_func_paint(grid,obj):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(G,(C,D))in obj:
		if 0<=C<E and 0<=D<F:B[C][D]=G
	return tuple(tuple(A)for A in B)
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
def val_func_adjacent(a,b):return val_func_manhattan(a,b)==1
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
def val_func_shape(piece):A=piece;return val_func_height(A),val_func_width(A)
def val_func_mostcolor(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
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
def val_func_insert(value,container):return container.union(frozenset({value}))
def val_func_last(container):return max(enumerate(container))[1]
def val_func_first(container):return next(iter(container))
def val_func_extract(container,condition):return next(A for A in container if condition(A))
def val_func_sfilter(container,condition):A=container;return type(A)(A for A in A if condition(A))
def val_func_tojvec(j):return 0,j
def val_func_toivec(i):return i,0
def val_func_crement(x):
	if isinstance(x,int):return 0 if x==0 else x+1 if x>0 else x-1
	return 0 if x[0]==0 else x[0]+1 if x[0]>0 else x[0]-1,0 if x[1]==0 else x[1]+1 if x[1]>0 else x[1]-1
def val_func_initset(value):return frozenset({value})
def val_func_difference(a,b):return type(a)(A for A in a if A not in b)
def val_func_intersection(a,b):return a&b
def val_func_combine(a,b):return type(a)((*a,*b))
def val_func_equality(a,b):return a==b
def val_func_invert(n):return-n if isinstance(n,int)else(-n[0],-n[1])
def val_func_multiply(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def val_func_identity(x):return x
def p(I):I=tuple(map(tuple,I));D=val_func_objects(I,False,True,True);Q=val_func_lbind(val_func_rbind,val_func_equality);R=val_func_rbind(val_func_compose,val_func_first);S=val_func_chain(R,Q,val_func_mostcolor);A=val_func_fork(val_func_sfilter,val_func_identity,S);E=val_func_fork(val_func_difference,val_func_identity,A);T=val_func_lbind(val_func_rbind,val_func_adjacent);U=val_func_rbind(val_func_compose,val_func_initset);V=val_func_chain(U,T,E);W=val_func_fork(val_func_extract,A,V);K=val_func_fork(val_func_insert,W,E);X=val_func_lbind(val_func_recolor,0);Y=val_func_chain(X,val_func_delta,K);Z=val_func_fork(val_func_combine,K,Y);B=val_func_fork(val_func_position,A,E);L=val_func_chain(val_func_toivec,val_func_first,B);M=val_func_chain(val_func_tojvec,val_func_last,B);a=val_func_fork(val_func_multiply,val_func_shape,L);b=val_func_fork(val_func_multiply,val_func_shape,M);c=val_func_fork(val_func_multiply,val_func_shape,B);d=val_func_fork(val_func_shift,val_func_hmirror,a);e=val_func_fork(val_func_shift,val_func_vmirror,b);f=val_func_compose(val_func_hmirror,val_func_vmirror);g=val_func_fork(val_func_shift,f,c);F=val_func_lbind(val_func_compose,A);h=F(d);i=F(e);j=F(g);k=val_func_compose(val_func_crement,val_func_invert);G=val_func_lbind(val_func_compose,k);l=G(L);m=G(M);n=G(B);N=val_func_fork(val_func_shift,h,l);O=val_func_fork(val_func_shift,i,m);P=val_func_fork(val_func_shift,j,n);H=val_func_lbind(val_func_index,I);C=val_func_lbind(val_func_compose,val_func_toindices);J=C(Z);o=C(N);p=C(O);q=C(P);r=val_func_fork(val_func_intersection,J,o);s=val_func_fork(val_func_intersection,J,p);t=val_func_fork(val_func_intersection,J,q);u=val_func_chain(H,val_func_first,r);v=val_func_chain(H,val_func_first,s);w=val_func_chain(H,val_func_first,t);x=val_func_fork(val_func_recolor,u,N);y=val_func_fork(val_func_recolor,v,O);z=val_func_fork(val_func_recolor,w,P);A0=mval_func_apply(x,D);A1=mval_func_apply(y,D);A2=mval_func_apply(z,D);A3=val_func_paint(I,A0);A4=val_func_paint(A3,A1);A5=val_func_paint(A4,A2);return[*map(list,A5)]