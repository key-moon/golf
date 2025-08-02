_A=True
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_ival_func_neighbors(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(A):return val_func_dval_func_neighbors(A)|val_func_ival_func_neighbors(A)
def val_func_dval_func_neighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def val_func_mostcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_lrcorner(A):return tuple(map(max,zip(*val_func_toindices(A))))
def val_func_crop(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_height(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def val_func_shape(A):return val_func_height(A),val_func_width(A)
def val_func_occurrences(A,B):
	C=set();K=val_func_normalize(B);D,E=len(A),len(A[0]);L,M=val_func_shape(B);N,O=D-L+1,E-M+1
	for F in range(N):
		for G in range(O):
			H=_A
			for(P,(I,J))in val_func_shift(K,(F,G)):
				if not(0<=I<D and 0<=J<E and A[I][J]==P):H=False;break
			if H:C.add((F,G))
	return frozenset(C)
def val_func_switch(A,B,C):return tuple(tuple(A if A!=B and A!=C else{B:C,C:B}[A]for A in A)for A in A)
def val_func_subgrid(A,B):return val_func_crop(B,val_func_ulcorner(A),val_func_shape(A))
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
def val_func_numcolors(A):return len(val_func_palette(A))
def val_func_palette(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_objects(A,B,C,D):
	K=val_func_mostcolor(A)if D else None;L=set();G=set();O,P=len(A),len(A[0]);Q=val_func_asindices(A);R=val_func_neighbors if C else val_func_dval_func_neighbors
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
def val_func_recolor(A,B):return frozenset((A,B)for B in val_func_toindices(B))
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_colorcount(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def mval_func_apply(A,B):return val_func_merge(val_func_apply(A,B))
def val_func_rval_func_apply(A,B):return type(A)(A(B)for A in A)
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
def val_func_matcher(A,B):return lambda C:A(C)==B
def val_func_chain(A,B,C):return lambda D:A(B(C(D)))
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_product(A,B):return frozenset((C,B)for B in B for C in A)
def val_func_astuple(A,B):return A,B
def val_func_remove(A,B):return type(B)(B for B in B if B!=A)
def val_func_last(A):return max(enumerate(A))[1]
def val_func_first(A):return next(iter(A))
def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_positive(A):return A>0
def val_func_argmax(A,B):return max(A,key=B)
def val_func_size(A):return len(A)
def val_func_greater(A,B):return A>B
def val_func_combine(A,B):return type(A)((*A,*B))
def val_func_contained(A,B):return A in B
def val_func_equality(A,B):return A==B
def val_func_flip(A):return not A
def val_func_subtract(A,B):
	if isinstance(A,int)and isinstance(B,int):return A-B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]-B[0],A[1]-B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A-B[0],A-B[1]
	return A[0]-B,A[1]-B
def p(A):A=tuple(map(tuple,A));B=val_func_objects(A,False,_A,_A);Q=val_func_argmax(B,val_func_size);C=val_func_subgrid(Q,A);R=val_func_rbind(val_func_greater,1);S=val_func_compose(R,val_func_numcolors);D=val_func_sfilter(B,S);T=val_func_lbind(val_func_rbind,val_func_subtract);E=val_func_switch(C,2,0);U=val_func_lbind(val_func_occurrences,E);V=val_func_lbind(val_func_lbind,val_func_shift);W=val_func_compose(T,val_func_ulcorner);F=val_func_matcher(val_func_first,2);X=val_func_compose(val_func_flip,F);Y=val_func_rbind(val_func_sfilter,F);Z=val_func_rbind(val_func_sfilter,X);a=val_func_lbind(val_func_recolor,0);b=val_func_compose(a,Z);G=val_func_fork(val_func_combine,b,Y);H=val_func_chain(W,G,val_func_normalize);c=val_func_objects(E,_A,_A,_A);d=val_func_apply(val_func_toindices,c);I=val_func_chain(U,G,val_func_normalize);e=val_func_rbind(val_func_colorcount,2);J=val_func_lbind(val_func_sfilter,d);f=val_func_chain(val_func_size,val_func_first,J);g=val_func_compose(val_func_positive,val_func_size);K=val_func_lbind(val_func_lbind,val_func_contained);h=val_func_chain(g,J,K);i=val_func_compose(f,K);j=val_func_rbind(val_func_sfilter,h);k=val_func_compose(j,I);l=val_func_lbind(val_func_rbind,val_func_equality);m=val_func_rbind(val_func_compose,i);n=val_func_chain(m,l,e);o=val_func_fork(val_func_sfilter,k,n);p=val_func_fork(val_func_apply,H,o);L=val_func_compose(V,val_func_normalize);q=val_func_fork(mval_func_apply,L,p);r=val_func_astuple(val_func_cmirror,val_func_dmirror);s=val_func_astuple(val_func_hmirror,val_func_vmirror);M=val_func_combine(r,s);t=val_func_product(M,M);u=val_func_fork(val_func_compose,val_func_first,val_func_last);v=val_func_apply(u,t);N=val_func_lbind(val_func_rval_func_apply,v);w=mval_func_apply(N,D);O=mval_func_apply(q,w);x=val_func_paint(C,O);y=val_func_palette(O);P=val_func_lbind(val_func_remove,2);z=P(y);À=val_func_chain(val_func_first,P,val_func_palette);Á=val_func_rbind(val_func_contained,z);Â=val_func_chain(val_func_flip,Á,À);Ã=val_func_sfilter(D,Â);Ä=val_func_fork(val_func_apply,H,I);Å=val_func_fork(mval_func_apply,L,Ä);Æ=mval_func_apply(N,Ã);Ç=mval_func_apply(Å,Æ);È=val_func_paint(x,Ç);return[*map(list,È)]