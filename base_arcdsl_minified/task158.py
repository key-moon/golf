def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def ival_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(loc):return val_func_dval_func_neighbors(loc)|ival_func_neighbors(loc)
def val_func_dval_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
def val_func_palette(element):
	A=element
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_lrcorner(patch):return tuple(map(max,zip(*val_func_toindices(patch))))
def val_func_ulcorner(patch):return tuple(map(min,zip(*val_func_toindices(patch))))
def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
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
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
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
def val_func_upscale(element,factor):
	B=element;A=factor
	if isinstance(B,tuple):
		C=tuple()
		for I in B:
			D=tuple()
			for E in I:D=D+tuple(E for A in range(A))
			C=C+tuple(D for A in range(A))
		return C
	else:
		if len(B)==0:return frozenset()
		F,G=val_func_ulcorner(B);J,K=-F,-G;L=val_func_shift(B,(J,K));H=set()
		for(E,(M,N))in L:
			for O in range(A):
				for P in range(A):H.add((E,(M*A+O,N*A+P)))
		return val_func_shift(frozenset(H),(F,G))
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
def val_func_numcolors(element):return len(val_func_palette(element))
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
def val_func_mostcolor(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def mval_func_apply(function,container):return val_func_merge(val_func_apply(function,container))
def val_func_rval_func_apply(functions,value):A=functions;return type(A)(A(value)for A in A)
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
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_product(a,b):return frozenset((B,A)for A in b for B in a)
def val_func_interval(start,stop,step):return tuple(range(start,stop,step))
def val_func_insert(value,container):return container.union(frozenset({value}))
def val_func_last(container):return max(enumerate(container))[1]
def val_func_first(container):return next(iter(container))
def val_func_sfilter(container,condition):A=container;return type(A)(A for A in A if condition(A))
def val_func_initset(value):return frozenset({value})
def val_func_argmax(container,compfunc):return max(container,key=compfunc)
def val_func_difference(a,b):return type(a)(A for A in a if A not in b)
def val_func_identity(x):return x
def p(I):I=tuple(map(tuple,I));A=val_func_objects(I,False,True,True);B=val_func_argmax(A,val_func_numcolors);C=val_func_normalize(B);D=val_func_lbind(val_func_matcher,val_func_first);E=val_func_compose(D,val_func_mostcolor);F=val_func_fork(val_func_sfilter,val_func_identity,E);G=val_func_fork(val_func_difference,val_func_identity,F);H=val_func_lbind(val_func_rbind,val_func_upscale);J=val_func_interval(1,4,1);K=val_func_apply(H,J);L=val_func_initset(val_func_identity);M=val_func_insert(val_func_vmirror,L);N=val_func_insert(val_func_hmirror,M);O=val_func_insert(val_func_cmirror,N);P=val_func_insert(val_func_dmirror,O);Q=val_func_fork(val_func_compose,val_func_first,val_func_last);R=val_func_lbind(val_func_occurrences,I);S=val_func_lbind(val_func_lbind,val_func_shift);T=val_func_compose(R,G);U=val_func_product(P,K);V=val_func_apply(Q,U);W=val_func_rval_func_apply(V,C);X=val_func_fork(mval_func_apply,S,T);Y=mval_func_apply(X,W);Z=val_func_paint(I,Y);return[*map(list,Z)]