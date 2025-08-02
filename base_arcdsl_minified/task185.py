def val_func_ival_func_neighbors(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(A):return val_func_dval_func_neighbors(A)|val_func_ival_func_neighbors(A)
def val_func_dval_func_neighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def val_func_mostval_func_color(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_crop(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def val_func_shape(A):return val_func_height(A),val_func_width(A)
def val_func_lrcorner(A):return tuple(map(max,zip(*val_func_toindices(A))))
def val_func_llcorner(A):return tuple(map(lambda B:{0:max,1:min}[B[0]](B[1]),enumerate(zip(*val_func_toindices(A)))))
def val_func_urcorner(A):return tuple(map(lambda B:{0:min,1:max}[B[0]](B[1]),enumerate(zip(*val_func_toindices(A)))))
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
def val_func_frontiers(A):C,D=len(A),len(A[0]);B=tuple(A for(A,B)in enumerate(A)if len(set(B))==1);E=tuple(A for(A,B)in enumerate(val_func_dmirror(A))if len(set(B))==1);F=frozenset({frozenset({(A[B][C],(B,C))for C in range(D)})for B in B});G=frozenset({frozenset({(A[C][B],(C,B))for C in range(C)})for B in E});return F|G
def val_func_outbox(A):F,G=val_func_uppermost(A)-1,val_func_leftmost(A)-1;H,I=val_func_lowermost(A)+1,val_func_rightmost(A)+1;B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def val_func_corners(A):return frozenset({val_func_ulcorner(A),val_func_urcorner(A),val_func_llcorner(A),val_func_lrcorner(A)})
def val_func_subgrid(A,B):return val_func_crop(B,val_func_ulcorner(A),val_func_shape(A))
def val_func_downscale(A,B):
	E,I=len(A),len(A[0]);C=tuple()
	for D in range(E):
		F=tuple()
		for H in range(I):
			if H%B==0:F=F+(A[D][H],)
		C=C+(F,)
	E=len(C);G=tuple()
	for D in range(E):
		if D%B==0:G=G+(C[D],)
	return G
def val_func_paint(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def val_func_dmirror(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_toobject(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in val_func_toindices(A)if 0<=A<D and 0<=C<E)
def val_func_color(A):return next(iter(A))[0]
def val_func_numval_func_colors(A):return len(val_func_palette(A))
def val_func_palette(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
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
def reval_func_color(A,B):return frozenset((A,B)for B in val_func_toindices(B))
def val_func_val_func_colorfilter(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def val_func_height(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def mval_func_apply(A,B):return val_func_merge(val_func_apply(A,B))
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_fork(A,B,C):return lambda D:A(B(D),C(D))
def val_func_power(A,B):
	if B==1:return A
	return val_func_compose(A,val_func_power(A,B-1))
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
def val_func_matcher(A,B):return lambda C:A(C)==B
def val_func_chain(A,B,C):return lambda D:A(B(C(D)))
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_pair(A,B):return tuple(zip(A,B))
def val_func_interval(A,B,C):return tuple(range(A,B,C))
def val_func_remove(A,B):return type(B)(B for B in B if B!=A)
def val_func_last(A):return max(enumerate(A))[1]
def val_func_first(A):return next(iter(A))
def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_increment(A):return A+1 if isinstance(A,int)else(A[0]+1,A[1]+1)
def val_func_both(A,B):return A and B
def val_func_argmax(A,B):return max(A,key=B)
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_size(A):return len(A)
def val_func_contained(A,B):return A in B
def val_func_flip(A):return not A
def val_func_identity(A):return A
def p(A):H=False;A=tuple(map(tuple,A));D=val_func_fgpartition(A);I=val_func_argmax(D,val_func_size);J=val_func_remove(I,D);K=val_func_merge(J);B=val_func_subgrid(K,A);L=val_func_chain(val_func_color,val_func_merge,val_func_frontiers);M=L(A);N=val_func_objects(B,True,H,H);E=val_func_val_func_colorfilter(N,0);O=val_func_rbind(val_func_toobject,B);C=val_func_chain(O,val_func_corners,val_func_outbox);P=val_func_lbind(val_func_contained,M);Q=val_func_chain(P,val_func_palette,C);R=val_func_compose(val_func_numval_func_colors,C);S=val_func_compose(val_func_flip,Q);T=val_func_matcher(R,1);U=val_func_fork(val_func_both,S,T);V=val_func_sfilter(E,U);W=val_func_compose(val_func_color,C);X=val_func_fork(reval_func_color,W,val_func_identity);Y=mval_func_apply(X,V);Z=val_func_paint(B,Y);a=val_func_first(E);F=val_func_height(a);G=val_func_height(B);b=val_func_increment(F);c=val_func_interval(0,G,b);d=val_func_interval(0,G,1);e=val_func_rbind(val_func_contained,c);f=val_func_chain(val_func_flip,e,val_func_last);g=val_func_lbind(val_func_apply,val_func_first);h=val_func_rbind(val_func_sfilter,f);i=val_func_rbind(val_func_pair,d);j=val_func_chain(g,h,i);k=val_func_compose(val_func_dmirror,j);l=val_func_power(k,2);m=l(Z);n=val_func_downscale(m,F);return[*map(list,n)]