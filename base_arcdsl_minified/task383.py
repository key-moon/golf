def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_ival_func_neighbors(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(A):return val_func_dval_func_neighbors(A)|val_func_ival_func_neighbors(A)
def val_func_dval_func_neighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_mostcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
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
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_height(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def val_func_crop(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def val_func_shape(A):return val_func_height(A),val_func_width(A)
def val_func_hfrontier(A):return frozenset((A[0],B)for B in range(30))
def val_func_vfrontier(A):return frozenset((B,A[1])for B in range(30))
def val_func_trim(A):return tuple(A[1:-1]for A in A[1:-1])
def val_func_subgrid(A,B):return val_func_crop(B,val_func_ulcorner(A),val_func_shape(A))
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_palette(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
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
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def val_func_leastcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def mval_func_apply(A,B):return val_func_merge(val_func_apply(A,B))
def val_func_fork(A,B,C):return lambda D:A(B(D),C(D))
def val_func_power(A,B):
	if B==1:return A
	return val_func_compose(A,val_func_power(A,B-1))
def val_func_matcher(A,B):return lambda C:A(C)==B
def val_func_other(A,B):return val_func_first(val_func_remove(B,A))
def val_func_remove(A,B):return type(B)(B for B in B if B!=A)
def val_func_first(A):return next(iter(A))
def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_either(A,B):return A or B
def val_func_difference(A,B):return type(A)(A for A in A if A not in B)
def val_func_intersection(A,B):return A&B
def val_func_combine(A,B):return type(A)((*A,*B))
def p(A):J=False;A=tuple(map(tuple,A));K=val_func_palette(A);L=val_func_objects(A,J,J,True);M=val_func_ofcolor(A,0);C=val_func_first(L);N=val_func_ulcorner(C);D=val_func_subgrid(C,A);O=val_func_power(val_func_trim,2);P=O(D);Q=val_func_asindices(P);R=val_func_shift(Q,(2,2));E=val_func_fill(D,0,R);B=val_func_leastcolor(E);S=val_func_remove(0,K);T=val_func_other(S,B);U=val_func_ofcolor(E,B);F=val_func_shift(U,N);G=val_func_ofcolor(A,B);V=val_func_uppermost(G);W=val_func_lowermost(G);X=val_func_matcher(val_func_first,V);Y=val_func_matcher(val_func_first,W);Z=val_func_fork(val_func_either,X,Y);H=val_func_sfilter(F,Z);a=val_func_difference(F,H);b=mval_func_apply(val_func_vfrontier,H);c=mval_func_apply(val_func_hfrontier,a);I=val_func_combine(b,c);d=val_func_intersection(M,I);e=val_func_fill(A,T,I);f=val_func_fill(e,B,d);return[*map(list,f)]