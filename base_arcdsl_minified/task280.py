def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def ival_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(loc):return val_func_dval_func_neighbors(loc)|ival_func_neighbors(loc)
def val_func_dval_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
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
def val_func_connect(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def val_func_shoot(start,direction):B=direction;A=start;return val_func_connect(A,(A[0]+42*B[0],A[1]+42*B[1]))
def val_func_center(patch):A=patch;return val_func_uppermost(A)+val_func_height(A)//2,val_func_leftmost(A)+val_func_width(A)//2
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
def val_func_vline(patch):A=patch;return val_func_height(A)==len(A)and val_func_width(A)==1
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
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
def val_func_shape(piece):A=piece;return val_func_height(A),val_func_width(A)
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
def val_func_matcher(function,target):return lambda x:function(x)==target
def val_func_chain(h,g,f):return lambda x:h(g(f(x)))
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_astuple(a,b):return a,b
def val_func_interval(start,stop,step):return tuple(range(start,stop,step))
def val_func_first(container):return next(iter(container))
def val_func_sfilter(container,condition):A=container;return type(A)(A for A in A if condition(A))
def val_func_tojvec(j):return 0,j
def val_func_toivec(i):return i,0
def val_func_decrement(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def val_func_increment(x):return x+1 if isinstance(x,int)else(x[0]+1,x[1]+1)
def val_func_minimum(container):return min(container,default=0)
def val_func_difference(a,b):return type(a)(A for A in a if A not in b)
def val_func_combine(a,b):return type(a)((*a,*b))
def val_func_equality(a,b):return a==b
def val_func_invert(n):return-n if isinstance(n,int)else(-n[0],-n[1])
def val_func_add(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):H=False;I=tuple(map(tuple,I));B=val_func_objects(I,H,H,True);J=val_func_matcher(val_func_first,2);A=val_func_rbind(val_func_sfilter,J);K=val_func_compose(val_func_lowermost,A);L=val_func_compose(val_func_rightmost,A);M=val_func_compose(val_func_uppermost,A);N=val_func_compose(val_func_leftmost,A);O=val_func_fork(val_func_equality,K,val_func_lowermost);P=val_func_fork(val_func_equality,L,val_func_rightmost);Q=val_func_fork(val_func_equality,M,val_func_uppermost);R=val_func_fork(val_func_equality,N,val_func_leftmost);S=val_func_compose(val_func_invert,Q);T=val_func_compose(val_func_invert,R);U=val_func_fork(val_func_add,S,O);V=val_func_fork(val_func_add,T,P);W=val_func_fork(val_func_astuple,U,V);X=val_func_compose(val_func_center,A);C=val_func_fork(val_func_shoot,X,W);Y=mval_func_apply(C,B);Z=val_func_fill(I,2,Y);a=val_func_compose(val_func_vline,C);D=val_func_sfilter(B,a);b=val_func_difference(B,D);E=val_func_chain(val_func_decrement,val_func_minimum,val_func_shape);c=val_func_compose(val_func_increment,E);d=val_func_compose(val_func_invert,E);e=val_func_rbind(val_func_interval,1);F=val_func_fork(e,d,c);f=val_func_lbind(val_func_apply,val_func_toivec);g=val_func_lbind(val_func_apply,val_func_tojvec);h=val_func_lbind(val_func_lbind,val_func_shift);G=val_func_compose(h,C);i=val_func_compose(f,F);j=val_func_compose(g,F);k=val_func_fork(mval_func_apply,G,i);l=val_func_fork(mval_func_apply,G,j);m=mval_func_apply(k,b);n=mval_func_apply(l,D);o=val_func_combine(m,n);p=underval_func_fill(Z,3,o);return[*map(list,p)]