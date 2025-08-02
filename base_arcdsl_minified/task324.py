def val_func_remove(A,B):return type(B)(B for B in B if B!=A)
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_ival_func_neighbors(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_dval_func_neighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_height(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def val_func_connect(A,B):
	C,D=A;E,F=B;G=min(C,E);H=max(C,E)+1;I=min(D,F);J=max(D,F)+1
	if C==E:return frozenset((C,A)for A in range(I,J))
	elif D==F:return frozenset((A,D)for A in range(G,H))
	elif E-C==F-D:return frozenset((A,B)for(A,B)in zip(range(G,H),range(I,J)))
	elif E-C==D-F:return frozenset((A,B)for(A,B)in zip(range(G,H),range(J-1,I-1,-1)))
	return frozenset()
def val_func_shoot(A,B):return val_func_connect(A,(A[0]+42*B[0],A[1]+42*B[1]))
def val_func_center(A):return val_func_uppermost(A)+val_func_height(A)//2,val_func_leftmost(A)+val_func_width(A)//2
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_toobject(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in val_func_toindices(A)if 0<=A<D and 0<=C<E)
def val_func_color(A):return next(iter(A))[0]
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
def val_func_neighbors(A):return val_func_dval_func_neighbors(A)|val_func_ival_func_neighbors(A)
def val_func_ofval_func_color(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_sizefilter(A,B):return frozenset(A for A in A if len(A)==B)
def val_func_mostval_func_color(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def mval_func_apply(A,B):return val_func_merge(val_func_apply(A,B))
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_fork(A,B,C):return lambda D:A(B(D),C(D))
def val_func_rbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(D,B)
	elif C==3:return lambda D,E:A(D,E,B)
	else:return lambda D,E,F:A(D,E,F,B)
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_branch(A,B,C):return B if A else C
def val_func_other(A,B):return val_func_first(val_func_remove(B,A))
def val_func_last(A):return max(enumerate(A))[1]
def val_func_first(A):return next(iter(A))
def val_func_difference(A,B):return type(A)(A for A in A if A not in B)
def val_func_intersection(A,B):return A&B
def val_func_combine(A,B):return type(A)((*A,*B))
def val_func_equality(A,B):return A==B
def p(A):K=False;A=tuple(map(tuple,A));D=val_func_objects(A,True,K,K);B=val_func_sizefilter(D,1);L=val_func_apply(val_func_color,B);M=val_func_difference(D,B);E=val_func_apply(val_func_color,M);F=val_func_first(E);N=val_func_last(E);O=val_func_ofval_func_color(A,F);P=val_func_ofval_func_color(A,N);Q=val_func_rbind(val_func_shoot,(1,1));R=val_func_rbind(val_func_shoot,(-1,-1));S=val_func_rbind(val_func_shoot,(1,-1));T=val_func_rbind(val_func_shoot,(-1,1));U=val_func_fork(val_func_combine,Q,R);V=val_func_fork(val_func_combine,S,T);W=val_func_fork(val_func_combine,U,V);X=val_func_compose(W,val_func_center);G=mval_func_apply(X,B);Y=val_func_intersection(O,G);Z=val_func_intersection(P,G);H=val_func_first(B);C=val_func_color(H);a=val_func_center(H);b=val_func_neighbors(a);c=val_func_toobject(b,A);d=val_func_mostval_func_color(c);I=val_func_other(L,C);J=val_func_equality(d,F);e=val_func_branch(J,C,I);f=val_func_branch(J,I,C);g=val_func_fill(A,e,Y);h=val_func_fill(g,f,Z);return[*map(list,h)]