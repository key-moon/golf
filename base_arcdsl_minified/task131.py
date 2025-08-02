def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_ival_func_neighbors(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(A):return val_func_dval_func_neighbors(A)|val_func_ival_func_neighbors(A)
def val_func_dval_func_neighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_mostcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_cover(A,B):return val_func_fill(A,val_func_mostcolor(A),val_func_toindices(B))
def val_func_manhattan(A,B):return min(abs(A-D)+abs(C-E)for(A,C)in val_func_toindices(A)for(D,E)in val_func_toindices(B))
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
def val_func_move(A,B,C):return val_func_paint(val_func_cover(A,B),val_func_shift(B,C))
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
def val_func_recolor(A,B):return frozenset((A,B)for B in val_func_toindices(B))
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_colorfilter(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_height(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def val_func_branch(A,B,C):return B if A else C
def val_func_first(A):return next(iter(A))
def val_func_sign(A):
	if isinstance(A,int):return 0 if A==0 else 1 if A>0 else-1
	return 0 if A[0]==0 else 1 if A[0]>0 else-1,0 if A[1]==0 else 1 if A[1]>0 else-1
def val_func_crement(A):
	if isinstance(A,int):return 0 if A==0 else A+1 if A>0 else A-1
	return 0 if A[0]==0 else A[0]+1 if A[0]>0 else A[0]-1,0 if A[1]==0 else A[1]+1 if A[1]>0 else A[1]-1
def val_func_equality(A,B):return A==B
def val_func_multiply(A,B):
	if isinstance(A,int)and isinstance(B,int):return A*B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]*B[0],A[1]*B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A*B[0],A*B[1]
	return A[0]*B,A[1]*B
def p(A):A=tuple(map(tuple,A));E=val_func_objects(A,True,False,True);F=val_func_colorfilter(E,3);B=val_func_first(F);C=val_func_ofcolor(A,2);D=val_func_gravitate(B,C);G=val_func_first(D);H=val_func_equality(G,0);I=val_func_branch(H,val_func_width,val_func_height);J=I(B);K=val_func_gravitate(C,B);L=val_func_sign(K);M=val_func_multiply(L,J);N=val_func_crement(M);O=val_func_recolor(8,C);P=val_func_shift(O,N);Q=val_func_paint(A,P);R=val_func_move(Q,B,D);return[*map(list,R)]