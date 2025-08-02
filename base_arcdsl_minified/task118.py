def val_func_sfilter(container,condition):A=container;return type(A)(A for A in A if condition(A))
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def ival_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(loc):return val_func_dval_func_neighbors(loc)|ival_func_neighbors(loc)
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
def val_func_mostcolor(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
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
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_toobject(patch,grid):A=grid;D,E=len(A),len(A[0]);return frozenset((A[B][C],(B,C))for(B,C)in val_func_toindices(patch)if 0<=B<D and 0<=C<E)
def val_func_hline(patch):A=patch;return val_func_width(A)==len(A)and val_func_height(A)==1
def val_func_vline(patch):A=patch;return val_func_height(A)==len(A)and val_func_width(A)==1
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
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def val_func_colorfilter(objs,value):return frozenset(A for A in objs if next(iter(A))[0]==value)
def val_func_colorcount(element,value):
	B=value;A=element
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def val_func_width(piece):
	A=piece
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_prval_func_apply(function,a,b):return frozenset(function(B,A)for A in b for B in a)
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
def val_func_insert(value,container):return container.union(frozenset({value}))
def val_func_mfilter(container,function):return val_func_merge(val_func_sfilter(container,function))
def val_func_tojvec(j):return 0,j
def val_func_toivec(i):return i,0
def val_func_either(a,b):return a or b
def val_func_both(a,b):return a and b
def val_func_initset(value):return frozenset({value})
def val_func_argmax(container,compfunc):return max(container,key=compfunc)
def val_func_valmax(container,compfunc):A=compfunc;return A(max(container,key=A,default=0))
def val_func_size(container):return len(container)
def val_func_greater(a,b):return a>b
def val_func_combine(a,b):return type(a)((*a,*b))
def val_func_halve(n):return n//2 if isinstance(n,int)else(n[0]//2,n[1]//2)
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
def p(I):G=False;I=tuple(map(tuple,I));A=val_func_ofcolor(I,2);H=val_func_prval_func_apply(val_func_connect,A,A);J=val_func_lbind(val_func_greater,6);K=val_func_compose(J,val_func_size);L=val_func_fork(val_func_either,val_func_vline,val_func_hline);M=val_func_fork(val_func_both,K,L);N=val_func_mfilter(H,M);B=val_func_fill(I,2,N);O=val_func_objects(B,True,G,G);C=val_func_colorfilter(O,2);P=val_func_valmax(C,val_func_width);D=val_func_halve(P);E=val_func_toivec(D);F=val_func_tojvec(D);Q=val_func_rbind(val_func_add,(0,2));R=val_func_rbind(val_func_add,(2,0));S=val_func_rbind(val_func_subtract,(0,2));T=val_func_rbind(val_func_subtract,(2,0));U=val_func_rbind(val_func_colorcount,2);V=val_func_rbind(val_func_toobject,B);W=val_func_compose(val_func_initset,Q);X=val_func_fork(val_func_insert,R,W);Y=val_func_fork(val_func_insert,S,X);Z=val_func_fork(val_func_insert,T,Y);a=val_func_fork(val_func_combine,val_func_dval_func_neighbors,Z);b=val_func_chain(U,V,a);c=val_func_rbind(val_func_argmax,b);d=val_func_compose(c,val_func_toindices);e=val_func_apply(d,C);f=val_func_rbind(val_func_add,E);g=val_func_rbind(val_func_subtract,E);h=val_func_rbind(val_func_add,F);i=val_func_rbind(val_func_subtract,F);j=val_func_fork(val_func_connect,f,g);k=val_func_fork(val_func_connect,h,i);l=val_func_fork(val_func_combine,j,k);m=mval_func_apply(l,e);n=val_func_fill(B,8,m);o=val_func_fill(n,2,A);return[*map(list,o)]