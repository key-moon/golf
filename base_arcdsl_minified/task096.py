def pval_func_apply(A,B,C):return tuple(A(B,C)for(B,C)in zip(B,C))
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
def val_func_ival_func_neighbors(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(A):return val_func_dval_func_neighbors(A)|val_func_ival_func_neighbors(A)
def val_func_dval_func_neighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def val_func_palette(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_lrcorner(A):return tuple(map(max,zip(*val_func_toindices(A))))
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_canvas(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def val_func_paint(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def val_func_cmirror(A):
	if isinstance(A,tuple):return tuple(zip(*(A[::-1]for A in A[::-1])))
	return val_func_vmirror(val_func_dmirror(val_func_vmirror(A)))
def val_func_dmirror(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_vmirror(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=val_func_ulcorner(A)[1]+val_func_lrcorner(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def val_func_hmirror(A):
	if isinstance(A,tuple):return A[::-1]
	B=val_func_ulcorner(A)[0]+val_func_lrcorner(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def val_func_rot90(A):return tuple(A for A in zip(*A[::-1]))
def val_func_color(A):return next(iter(A))[0]
def val_func_centerofmass(A):return tuple(map(lambda B:sum(B)//len(A),zip(*val_func_toindices(A))))
def val_func_manhattan(A,B):return min(abs(A-D)+abs(C-E)for(A,C)in val_func_toindices(A)for(D,E)in val_func_toindices(B))
def val_func_fgpartition(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in val_func_palette(A)-{val_func_mostval_func_color(A)})
def val_func_objects(A,B,C,D):
	K=val_func_mostval_func_color(A)if D else None;L=set();G=set();O,P=len(A),len(A[0]);Q=val_func_asindices(A);R=val_func_neighbors if C else val_func_dval_func_neighbors
	for E in Q:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==K:continue
		M={(H,E)};I={E}
		while len(I)>0:
			N=set()
			for F in I:
				J=A[F[0]][F[1]]
				if H==J if B else J!=K:M.add((J,F));G.add(F);N|={(A,B)for(A,B)in R(F)if 0<=A<O and 0<=B<P}
			I=N-G
		L.add(frozenset(M))
	return frozenset(L)
def val_func_normalize(A):
	if len(A)==0:return A
	return val_func_shift(A,(-val_func_uppermost(A),-val_func_leftmost(A)))
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_val_func_colorfilter(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_mostval_func_color(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def prval_func_apply(A,B,C):return frozenset(A(D,C)for C in C for D in B)
def mpval_func_apply(A,B,C):return val_func_merge(pval_func_apply(A,B,C))
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_fork(A,B,C):return lambda D:A(B(D),C(D))
def val_func_lbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(B,D)
	elif C==3:return lambda D,E:A(B,D,E)
	else:return lambda D,E,F:A(B,D,E,F)
def val_func_rbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(D,B)
	elif C==3:return lambda D,E:A(D,E,B)
	else:return lambda D,E,F:A(D,E,F,B)
def val_func_chain(A,B,C):return lambda D:A(B(C(D)))
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_branch(A,B,C):return B if A else C
def val_func_pair(A,B):return tuple(zip(A,B))
def val_func_astuple(A,B):return A,B
def val_func_interval(A,B,C):return tuple(range(A,B,C))
def val_func_remove(A,B):return type(B)(B for B in B if B!=A)
def val_func_insert(A,B):return B.union(frozenset({A}))
def val_func_positive(A):return A>0
def val_func_decrement(A):return A-1 if isinstance(A,int)else(A[0]-1,A[1]-1)
def val_func_increment(A):return A+1 if isinstance(A,int)else(A[0]+1,A[1]+1)
def val_func_initset(A):return frozenset({A})
def val_func_argmin(A,B):return min(A,key=B)
def val_func_valmax(A,B):return B(max(A,key=B,default=0))
def val_func_minimum(A):return min(A,default=0)
def val_func_size(A):return len(A)
def val_func_order(A,B):return tuple(sorted(A,key=B))
def val_func_contained(A,B):return A in B
def val_func_double(A):return A*2 if isinstance(A,int)else(A[0]*2,A[1]*2)
def val_func_invert(A):return-A if isinstance(A,int)else(-A[0],-A[1])
def val_func_add(A,B):
	if isinstance(A,int)and isinstance(B,int):return A+B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]+B[0],A[1]+B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A+B[0],A+B[1]
	return A[0]+B,A[1]+B
def val_func_identity(A):return A
def p(A):A=tuple(map(tuple,A));H=val_func_mostval_func_color(A);C=val_func_fgpartition(A);I=val_func_objects(A,True,False,True);J=val_func_rbind(val_func_valmax,val_func_width);K=val_func_lbind(val_func_val_func_colorfilter,I);L=val_func_compose(K,val_func_color);M=val_func_compose(val_func_double,J);N=val_func_lbind(prval_func_apply,val_func_manhattan);O=val_func_fork(N,val_func_identity,val_func_identity);P=val_func_lbind(val_func_remove,0);Q=val_func_compose(P,O);R=val_func_rbind(val_func_branch,-2);S=val_func_fork(R,val_func_positive,val_func_decrement);T=val_func_chain(S,val_func_minimum,Q);U=val_func_fork(val_func_add,T,M);V=val_func_compose(U,L);W=val_func_compose(val_func_invert,V);X=val_func_order(C,W);Y=val_func_rbind(val_func_argmin,val_func_centerofmass);Z=val_func_compose(val_func_initset,val_func_vmirror);a=val_func_fork(val_func_insert,val_func_dmirror,Z);b=val_func_fork(val_func_insert,val_func_cmirror,a);c=val_func_fork(val_func_insert,val_func_hmirror,b);d=val_func_compose(Y,c);e=val_func_apply(d,X);D=val_func_size(C);f=val_func_apply(val_func_size,C);g=val_func_contained(1,f);h=val_func_increment(D);E=val_func_branch(g,D,h);i=val_func_double(E);F=val_func_decrement(i);j=val_func_apply(val_func_normalize,e);G=val_func_interval(0,E,1);k=val_func_pair(G,G);B=mpval_func_apply(val_func_shift,j,k);l=val_func_astuple(F,F);m=val_func_canvas(H,l);n=val_func_paint(m,B);o=val_func_rot90(n);p=val_func_paint(o,B);q=val_func_rot90(p);r=val_func_paint(q,B);s=val_func_rot90(r);t=val_func_paint(s,B);return[*map(list,t)]