def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def ival_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
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
def val_func_normalize(patch):
	A=patch
	if len(A)==0:return A
	return val_func_shift(A,(-val_func_uppermost(A),-val_func_leftmost(A)))
def val_func_shape(piece):A=piece;return val_func_height(A),val_func_width(A)
def val_func_occurrences(grid,obj):
	A=grid;B=set();J=val_func_normalize(obj);C,D=len(A),len(A[0]);K,L=val_func_shape(obj);M,N=C-K+1,D-L+1
	for E in range(M):
		for F in range(N):
			G=True
			for(O,(H,I))in val_func_shift(J,(E,F)):
				if not(0<=H<C and 0<=I<D and A[H][I]==O):G=False;break
			if G:B.add((E,F))
	return frozenset(B)
def val_func_canvas(value,dimensions):A=dimensions;return tuple(tuple(value for A in range(A[1]))for B in range(A[0]))
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_asobject(grid):return frozenset((D,(A,C))for(A,B)in enumerate(grid)for(C,D)in enumerate(B))
def val_func_toobject(patch,grid):A=grid;D,E=len(A),len(A[0]);return frozenset((A[B][C],(B,C))for(B,C)in val_func_toindices(patch)if 0<=B<D and 0<=C<E)
def val_func_palette(element):
	A=element
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_bordering(patch,grid):A=patch;return val_func_uppermost(A)==0 or val_func_leftmost(A)==0 or val_func_lowermost(A)==len(grid)-1 or val_func_rightmost(A)==len(grid[0])-1
def val_func_neighbors(loc):return val_func_dval_func_neighbors(loc)|ival_func_neighbors(loc)
def val_func_dval_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_shift(patch,directions):
	A=patch
	if len(A)==0:return A
	B,C=directions
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(D+B,E+C))for(A,(D,E))in A)
	return frozenset((A+B,D+C)for(A,D)in A)
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
def val_func_colorcount(element,value):
	B=value;A=element
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
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
def val_func_matcher(function,target):return lambda x:function(x)==target
def val_func_chain(h,g,f):return lambda x:h(g(f(x)))
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_product(a,b):return frozenset((B,A)for A in b for B in a)
def val_func_astuple(a,b):return a,b
def val_func_interval(start,stop,step):return tuple(range(start,stop,step))
def val_func_last(container):return max(enumerate(container))[1]
def val_func_first(container):return next(iter(container))
def val_func_sfilter(container,condition):A=container;return type(A)(A for A in A if condition(A))
def val_func_positive(x):return x>0
def val_func_both(a,b):return a and b
def val_func_initset(value):return frozenset({value})
def val_func_argmax(container,compfunc):return max(container,key=compfunc)
def val_func_size(container):return len(container)
def val_func_contained(value,container):return value in container
def val_func_multiply(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def val_func_identity(x):return x
def p(I):I=tuple(map(tuple,I));H=val_func_asindices(I);J=val_func_fork(val_func_product,val_func_identity,val_func_identity);K=val_func_lbind(val_func_canvas,0);B=val_func_compose(val_func_asobject,K);L=val_func_fork(val_func_multiply,val_func_first,val_func_last);M=val_func_compose(val_func_positive,val_func_size);N=val_func_lbind(val_func_lbind,val_func_shift);O=val_func_rbind(val_func_fork,L);P=val_func_lbind(O,val_func_multiply);Q=val_func_lbind(val_func_chain,M);R=val_func_rbind(Q,B);S=val_func_lbind(val_func_lbind,val_func_occurrences);T=val_func_chain(P,R,S);U=val_func_compose(J,val_func_first);V=val_func_compose(T,val_func_last);D=val_func_fork(val_func_argmax,U,V);W=val_func_chain(N,B,D);X=val_func_compose(B,D);Y=val_func_fork(val_func_occurrences,val_func_last,X);C=val_func_fork(mval_func_apply,W,Y);Z=val_func_multiply(2,6);a=val_func_interval(3,Z,1);b=val_func_astuple(a,I);c=C(b);E=val_func_fill(I,3,c);F=val_func_interval(3,10,1);d=val_func_astuple(F,E);e=C(d);G=val_func_fill(E,3,e);f=val_func_astuple(F,G);g=C(f);h=val_func_fill(G,3,g);i=val_func_rbind(val_func_toobject,h);j=val_func_rbind(val_func_colorcount,3);k=val_func_chain(j,i,val_func_neighbors);l=val_func_matcher(k,8);m=val_func_sfilter(H,l);A=val_func_fill(I,3,m);n=val_func_ofcolor(A,0);o=val_func_rbind(val_func_bordering,A);p=val_func_compose(o,val_func_initset);q=val_func_lbind(val_func_contained,3);r=val_func_rbind(val_func_toobject,A);s=val_func_chain(q,val_func_palette,r);t=val_func_compose(s,val_func_dval_func_neighbors);u=val_func_fork(val_func_both,t,p);v=val_func_sfilter(n,u);w=val_func_fill(A,3,v);return[*map(list,w)]