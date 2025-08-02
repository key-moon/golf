def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_ival_func_neighbors(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(A):return val_func_dval_func_neighbors(A)|val_func_ival_func_neighbors(A)
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def val_func_mostcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_canvas(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def val_func_paint(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def val_func_palette(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
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
def val_func_dval_func_neighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
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
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
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
def val_func_astuple(A,B):return A,B
def val_func_other(A,B):return val_func_first(val_func_remove(B,A))
def val_func_remove(A,B):return type(B)(B for B in B if B!=A)
def val_func_last(A):return max(enumerate(A))[1]
def val_func_first(A):return next(iter(A))
def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_decrement(A):return A-1 if isinstance(A,int)else(A[0]-1,A[1]-1)
def val_func_initset(A):return frozenset({A})
def val_func_argmin(A,B):return min(A,key=B)
def val_func_size(A):return len(A)
def val_func_order(A,B):return tuple(sorted(A,key=B))
def val_func_intersection(A,B):return A&B
def val_func_combine(A,B):return type(A)((*A,*B))
def val_func_subtract(A,B):
	if isinstance(A,int)and isinstance(B,int):return A-B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]-B[0],A[1]-B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A-B[0],A-B[1]
	return A[0]-B,A[1]-B
def val_func_add(A,B):
	if isinstance(A,int)and isinstance(B,int):return A+B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]+B[0],A[1]+B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A+B[0],A+B[1]
	return A[0]+B,A[1]+B
def val_func_identity(A):return A
def p(A):G=False;A=tuple(map(tuple,A));B=val_func_objects(A,G,G,True);H=val_func_rbind(val_func_other,5);I=val_func_compose(H,val_func_palette);J=val_func_fork(val_func_recolor,I,val_func_identity);K=val_func_apply(J,B);L=val_func_order(K,val_func_leftmost);M=val_func_compose(val_func_last,val_func_last);C=val_func_lbind(val_func_matcher,M);N=val_func_compose(C,val_func_leftmost);O=val_func_compose(C,val_func_rightmost);P=val_func_fork(val_func_sfilter,val_func_identity,N);Q=val_func_fork(val_func_sfilter,val_func_identity,O);R=val_func_compose(val_func_dval_func_neighbors,val_func_last);S=val_func_rbind(val_func_chain,R);T=val_func_lbind(S,val_func_size);U=val_func_lbind(val_func_rbind,val_func_intersection);D=val_func_chain(T,U,val_func_toindices);V=val_func_fork(val_func_argmin,P,D);W=val_func_fork(val_func_argmin,Q,D);X=val_func_compose(val_func_last,V);Y=val_func_compose(val_func_last,W);Z=val_func_astuple(0,(1,-1));a=val_func_initset(Z);b=val_func_lbind(val_func_add,(0,1));c=val_func_chain(X,val_func_first,val_func_last);d=val_func_compose(Y,val_func_first);e=val_func_fork(val_func_subtract,d,c);E=val_func_compose(val_func_first,val_func_last);f=val_func_compose(b,e);g=val_func_fork(val_func_shift,E,f);h=val_func_fork(val_func_combine,val_func_first,g);i=val_func_fork(val_func_remove,E,val_func_last);j=val_func_fork(val_func_astuple,h,i);k=val_func_size(B);l=val_func_power(j,k);m=val_func_astuple(a,L);n=l(m);F=val_func_first(n);o=val_func_width(F);p=val_func_decrement(o);q=val_func_astuple(3,p);r=val_func_canvas(0,q);s=val_func_paint(r,F);return[*map(list,s)]