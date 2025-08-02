def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_ival_func_neighbors(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(A):return val_func_dval_func_neighbors(A)|val_func_ival_func_neighbors(A)
def val_func_dval_func_neighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def val_func_mostcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_manhattan(A,B):return min(abs(A-D)+abs(C-E)for(A,C)in val_func_toindices(A)for(D,E)in val_func_toindices(B))
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
def val_func_center(A):return val_func_uppermost(A)+val_func_height(A)//2,val_func_leftmost(A)+val_func_width(A)//2
def val_func_adjacent(A,B):return val_func_manhattan(A,B)==1
def val_func_vmatching(A,B):return len(set(A for(B,A)in val_func_toindices(A))&set(A for(B,A)in val_func_toindices(B)))>0
def val_func_gravitate(A,B):
	H,I=val_func_center(A);J,K=val_func_center(B);C,D=0,0
	if val_func_vmatching(A,B):C=1 if H<J else-1
	else:D=1 if I<K else-1
	E,F=C,D;G=0
	while not val_func_adjacent(A,B)and G<42:G+=1;E+=C;F+=D;A=val_func_shift(A,(C,D))
	return E-C,F-D
def val_func_replace(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def val_func_paint(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
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
def val_func_colorfilter(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def mval_func_apply(A,B):return val_func_merge(val_func_apply(A,B))
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
def val_func_first(A):return next(iter(A))
def val_func_identity(A):return A
def p(A):A=tuple(map(tuple,A));D=val_func_objects(A,True,False,True);E=val_func_replace(A,3,0);F=val_func_replace(E,7,0);B=val_func_lbind(val_func_colorfilter,D);G=val_func_lbind(val_func_rbind,val_func_gravitate);C=val_func_chain(G,val_func_first,B);H=C(2);I=C(1);J=B(3);K=B(7);L=val_func_fork(val_func_shift,val_func_identity,H);M=val_func_fork(val_func_shift,val_func_identity,I);N=mval_func_apply(L,J);O=mval_func_apply(M,K);P=val_func_paint(F,N);Q=val_func_paint(P,O);return[*map(list,Q)]