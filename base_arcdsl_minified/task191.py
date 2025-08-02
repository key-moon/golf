def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
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
def val_func_crop(grid,start,dims):A=start;return tuple(B[A[1]:A[1]+dims[1]]for B in grid[A[0]:A[0]+dims[0]])
def val_func_shape(piece):A=piece;return val_func_height(A),val_func_width(A)
def val_func_subgrid(patch,grid):A=patch;return val_func_crop(grid,val_func_ulcorner(A),val_func_shape(A))
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_rot270(grid):return tuple(tuple(A[::-1])for A in zip(*grid[::-1]))[::-1]
def val_func_rot180(grid):return tuple(tuple(A[::-1])for A in grid[::-1])
def val_func_rot90(grid):return tuple(A for A in zip(*grid[::-1]))
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
def val_func_ulcorner(patch):return tuple(map(min,zip(*val_func_toindices(patch))))
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
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
def val_func_mval_func_pval_func_apply(function,a,b):return val_func_merge(val_func_pval_func_apply(function,a,b))
def val_func_pval_func_apply(function,a,b):return tuple(function(A,B)for(A,B)in zip(a,b))
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
def val_func_product(a,b):return frozenset((B,A)for A in b for B in a)
def val_func_astuple(a,b):return a,b
def val_func_interval(start,stop,step):return tuple(range(start,stop,step))
def val_func_sfilter(container,condition):A=container;return type(A)(A for A in A if condition(A))
def val_func_increment(x):return x+1 if isinstance(x,int)else(x[0]+1,x[1]+1)
def val_func_size(container):return len(container)
def val_func_difference(a,b):return type(a)(A for A in a if A not in b)
def val_func_combine(a,b):return type(a)((*a,*b))
def val_func_subtract(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):I=tuple(map(tuple,I));H=val_func_height(I);J=val_func_width(I);B=val_func_ofcolor(I,1);K=val_func_ofcolor(I,4);L=val_func_ulcorner(B);A=val_func_subgrid(B,I);M=val_func_rot90(A);N=val_func_rot180(A);O=val_func_rot270(A);P=val_func_matcher(val_func_size,0);Q=val_func_rbind(val_func_ofcolor,1);R=val_func_compose(val_func_normalize,Q);S=val_func_rbind(val_func_ofcolor,4);T=val_func_rbind(val_func_shift,L);U=val_func_compose(T,S);V=val_func_lbind(val_func_subtract,H);W=val_func_chain(val_func_increment,V,val_func_height);X=val_func_lbind(val_func_subtract,J);Y=val_func_chain(val_func_increment,X,val_func_width);Z=val_func_rbind(val_func_interval,1);C=val_func_lbind(Z,0);a=val_func_compose(C,W);b=val_func_compose(C,Y);c=val_func_fork(val_func_product,a,b);d=val_func_rbind(val_func_shift,(-1,-1));D=val_func_lbind(val_func_lbind,val_func_shift);e=val_func_chain(D,d,R);f=val_func_astuple(A,M);g=val_func_astuple(N,O);E=val_func_combine(f,g);F=val_func_apply(U,E);h=val_func_lbind(val_func_difference,K);i=val_func_apply(h,F);G=val_func_apply(val_func_normalize,F);j=val_func_apply(c,G);k=val_func_lbind(val_func_rbind,val_func_difference);l=val_func_apply(D,G);m=val_func_apply(k,i);n=val_func_pval_func_apply(val_func_compose,m,l);o=val_func_lbind(val_func_compose,P);p=val_func_apply(o,n);q=val_func_pval_func_apply(val_func_sfilter,j,p);r=val_func_apply(e,E);s=val_func_mval_func_pval_func_apply(mval_func_apply,r,q);t=val_func_fill(I,1,s);return[*map(list,t)]