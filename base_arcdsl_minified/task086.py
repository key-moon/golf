def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_ival_func_neighbors(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(A):return val_func_dval_func_neighbors(A)|val_func_ival_func_neighbors(A)
def val_func_dval_func_neighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def val_func_mostcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_llcorner(A):return tuple(map(lambda B:{0:max,1:min}[B[0]](B[1]),enumerate(zip(*val_func_toindices(A)))))
def val_func_urcorner(A):return tuple(map(lambda B:{0:min,1:max}[B[0]](B[1]),enumerate(zip(*val_func_toindices(A)))))
def val_func_lrcorner(A):return tuple(map(max,zip(*val_func_toindices(A))))
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
def val_func_outbox(A):F,G=val_func_uppermost(A)-1,val_func_leftmost(A)-1;H,I=val_func_lowermost(A)+1,val_func_rightmost(A)+1;B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def val_func_inbox(A):F,G=val_func_uppermost(A)+1,val_func_leftmost(A)+1;H,I=val_func_lowermost(A)-1,val_func_rightmost(A)-1;B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def val_func_backdrop(A):
	if len(A)==0:return frozenset({})
	B=val_func_toindices(A);C,D=val_func_ulcorner(B);E,F=val_func_lrcorner(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def val_func_corners(A):return frozenset({val_func_ulcorner(A),val_func_urcorner(A),val_func_llcorner(A),val_func_lrcorner(A)})
def val_func_switch(A,B,C):return tuple(tuple(A if A!=B and A!=C else{B:C,C:B}[A]for A in A)for A in A)
def underval_func_fill(A,B,C):
	G,H=len(A),len(A[0]);I=val_func_mostcolor(A);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
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
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_leastcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def mval_func_apply(A,B):return val_func_merge(val_func_apply(A,B))
def val_func_rval_func_apply(A,B):return type(A)(A(B)for A in A)
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
def val_func_chain(A,B,C):return lambda D:A(B(C(D)))
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_other(A,B):return val_func_first(val_func_remove(B,A))
def val_func_remove(A,B):return type(B)(B for B in B if B!=A)
def val_func_first(A):return next(iter(A))
def val_func_initset(A):return frozenset({A})
def val_func_intersection(A,B):return A&B
def val_func_identity(A):return A
def p(A):G=False;A=tuple(map(tuple,A));C=val_func_objects(A,G,G,True);D=val_func_leastcolor(A);H=val_func_palette(A);I=val_func_remove(0,H);E=val_func_other(I,D);J=val_func_switch(A,D,E);K=val_func_compose(val_func_width,val_func_inbox);L=val_func_lbind(val_func_power,val_func_outbox);F=val_func_compose(L,K);M=val_func_initset(F);N=val_func_lbind(val_func_rval_func_apply,M);O=val_func_chain(val_func_initset,val_func_first,N);P=val_func_fork(val_func_rval_func_apply,O,val_func_identity);Q=val_func_compose(val_func_first,P);B=val_func_compose(val_func_backdrop,Q);R=val_func_lbind(val_func_chain,val_func_backdrop);S=val_func_lbind(R,val_func_inbox);T=val_func_compose(S,F);U=val_func_lbind(val_func_apply,val_func_initset);V=val_func_chain(U,val_func_corners,B);W=val_func_fork(mval_func_apply,T,V);X=val_func_fork(val_func_intersection,B,W);Y=mval_func_apply(B,C);Z=mval_func_apply(X,C);a=underval_func_fill(J,E,Y);b=val_func_fill(a,0,Z);return[*map(list,b)]