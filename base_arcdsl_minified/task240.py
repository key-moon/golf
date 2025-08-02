def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
def val_func_palette(element):
	A=element
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_mostval_func_color(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_lefthalf(grid):return val_func_rot270(val_func_tophalf(val_func_rot90(grid)))
def val_func_tophalf(grid):return grid[:len(grid)//2]
def val_func_cover(grid,patch):return val_func_fill(grid,val_func_mostval_func_color(grid),val_func_toindices(patch))
def val_func_connect(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
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
def val_func_rot270(grid):return tuple(tuple(A[::-1])for A in zip(*grid[::-1]))[::-1]
def val_func_rot180(grid):return tuple(tuple(A[::-1])for A in grid[::-1])
def val_func_rot90(grid):return tuple(A for A in zip(*grid[::-1]))
def val_func_color(obj):return next(iter(obj))[0]
def val_func_numval_func_colors(element):return len(val_func_palette(element))
def val_func_partition(grid):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(grid)for(E,A)in enumerate(D)if A==B)for B in val_func_palette(grid))
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
def val_func_reval_func_color(value,patch):return frozenset((value,A)for A in val_func_toindices(patch))
def val_func_lrcorner(patch):return tuple(map(max,zip(*val_func_toindices(patch))))
def val_func_llcorner(patch):return tuple(map(lambda ix:{0:max,1:min}[ix[0]](ix[1]),enumerate(zip(*val_func_toindices(patch)))))
def val_func_urcorner(patch):return tuple(map(lambda ix:{0:min,1:max}[ix[0]](ix[1]),enumerate(zip(*val_func_toindices(patch)))))
def val_func_ulcorner(patch):return tuple(map(min,zip(*val_func_toindices(patch))))
def val_func_sizefilter(container,n):return frozenset(A for A in container if len(A)==n)
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
def val_func_chain(h,g,f):return lambda x:h(g(f(x)))
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_pair(a,b):return tuple(zip(a,b))
def val_func_insert(value,container):return container.union(frozenset({value}))
def val_func_last(container):return max(enumerate(container))[1]
def val_func_sfilter(container,condition):A=container;return type(A)(A for A in A if condition(A))
def val_func_tojvec(j):return 0,j
def val_func_initset(value):return frozenset({value})
def val_func_argmax(container,compfunc):return max(container,key=compfunc)
def val_func_maximum(container):return max(container,default=0)
def val_func_combine(a,b):return type(a)((*a,*b))
def val_func_even(n):return n%2==0
def val_func_add(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):I=tuple(map(tuple,I));G=val_func_rot90(I);H=val_func_rot180(I);J=val_func_rot270(I);K=val_func_initset(I);L=val_func_chain(val_func_numval_func_colors,val_func_lefthalf,val_func_tophalf);M=val_func_insert(G,K);N=val_func_insert(H,M);O=val_func_insert(J,N);D=val_func_argmax(O,L);P=val_func_vmirror(D);Q=val_func_pval_func_apply(val_func_pair,D,P);A=val_func_lbind(val_func_apply,val_func_maximum);E=val_func_apply(A,Q);R=val_func_partition(E);C=val_func_sizefilter(R,4);S=val_func_apply(val_func_llcorner,C);T=val_func_apply(val_func_lrcorner,C);U=val_func_combine(S,T);V=val_func_cover(E,U);W=val_func_tojvec(-2);X=val_func_rbind(val_func_add,(0,2));Y=val_func_rbind(val_func_add,W);F=val_func_compose(X,val_func_ulcorner);Z=val_func_compose(Y,val_func_urcorner);a=val_func_fork(val_func_connect,F,Z);b=val_func_compose(val_func_even,val_func_last);c=val_func_rbind(val_func_sfilter,b);d=val_func_chain(val_func_normalize,c,a);e=val_func_fork(val_func_shift,d,F);f=val_func_fork(val_func_reval_func_color,val_func_color,e);g=mval_func_apply(f,C);B=val_func_paint(V,g);h=val_func_rot90(B);i=val_func_rot180(B);j=val_func_rot270(B);k=val_func_pval_func_apply(val_func_pair,B,h);l=val_func_apply(A,k);m=val_func_pval_func_apply(val_func_pair,l,i);n=val_func_apply(A,m);o=val_func_pval_func_apply(val_func_pair,n,j);p=val_func_apply(A,o);return[*map(list,p)]