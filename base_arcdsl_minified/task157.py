def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def ival_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(loc):return val_func_dval_func_neighbors(loc)|ival_func_neighbors(loc)
def val_func_dval_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_mostcolor(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_lrcorner(patch):return tuple(map(max,zip(*val_func_toindices(patch))))
def val_func_ulcorner(patch):return tuple(map(min,zip(*val_func_toindices(patch))))
def val_func_backdrop(patch):
	A=patch
	if len(A)==0:return frozenset({})
	B=val_func_toindices(A);C,D=val_func_ulcorner(B);E,F=val_func_lrcorner(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_outbox(patch):A=patch;F,G=val_func_uppermost(A)-1,val_func_leftmost(A)-1;H,I=val_func_lowermost(A)+1,val_func_rightmost(A)+1;B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def val_func_delta(patch):
	A=patch
	if len(A)==0:return frozenset({})
	return val_func_backdrop(A)-val_func_toindices(A)
def val_func_cover(grid,patch):return val_func_fill(grid,val_func_mostcolor(grid),val_func_toindices(patch))
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
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
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_crop(grid,start,dims):A=start;return tuple(B[A[1]:A[1]+dims[1]]for B in grid[A[0]:A[0]+dims[0]])
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
def val_func_colorfilter(objs,value):return frozenset(A for A in objs if next(iter(A))[0]==value)
def val_func_width(piece):
	A=piece
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
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
def val_func_argmax(container,compfunc):return max(container,key=compfunc)
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_size(container):return len(container)
def val_func_intersection(a,b):return a&b
def val_func_invert(n):return-n if isinstance(n,int)else(-n[0],-n[1])
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
def p(I):I=tuple(map(tuple,I));F=val_func_width(I);G=val_func_objects(I,True,False,True);H=val_func_astuple(5,F);A=val_func_crop(I,(0,0),H);B=val_func_colorfilter(G,5);J=val_func_merge(B);K=val_func_cover(I,J);L=val_func_compose(val_func_toindices,val_func_normalize);M=val_func_apply(L,B);C=val_func_asindices(A);N=val_func_ofcolor(A,0);O=val_func_ofcolor(A,2);D=val_func_rbind(val_func_multiply,10);P=val_func_rbind(val_func_multiply,5);Q=val_func_rbind(val_func_intersection,O);E=val_func_rbind(val_func_intersection,N);R=val_func_rbind(val_func_intersection,C);S=val_func_chain(D,val_func_size,Q);T=val_func_chain(val_func_size,E,val_func_delta);U=val_func_compose(P,val_func_uppermost);V=val_func_chain(val_func_size,E,val_func_outbox);W=val_func_chain(D,val_func_size,R);X=val_func_compose(val_func_invert,S);Y=val_func_fork(val_func_add,W,X);Z=val_func_fork(val_func_subtract,Y,V);a=val_func_fork(val_func_subtract,Z,U);b=val_func_fork(val_func_subtract,a,T);c=val_func_rbind(val_func_apply,C);d=val_func_lbind(val_func_lbind,val_func_shift);e=val_func_rbind(val_func_argmax,b);f=val_func_chain(e,c,d);g=mval_func_apply(f,M);h=val_func_fill(K,1,g);return[*map(list,h)]