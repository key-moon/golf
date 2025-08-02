def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_merge(A):return type(A)(B for A in A for B in A)
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
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_connect(A,B):
	C,D=A;E,F=B;G=min(C,E);H=max(C,E)+1;I=min(D,F);J=max(D,F)+1
	if C==E:return frozenset((C,A)for A in range(I,J))
	elif D==F:return frozenset((A,D)for A in range(G,H))
	elif E-C==F-D:return frozenset((A,B)for(A,B)in zip(range(G,H),range(I,J)))
	elif E-C==D-F:return frozenset((A,B)for(A,B)in zip(range(G,H),range(J-1,I-1,-1)))
	return frozenset()
def val_func_shoot(A,B):return val_func_connect(A,(A[0]+42*B[0],A[1]+42*B[1]))
def val_func_inbox(A):F,G=val_func_uppermost(A)+1,val_func_leftmost(A)+1;H,I=val_func_lowermost(A)-1,val_func_rightmost(A)-1;B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def val_func_cover(A,B):return val_func_fill(A,val_func_mostcolor(A),val_func_toindices(B))
def underval_func_fill(A,B,C):
	G,H=len(A),len(A[0]);I=val_func_mostcolor(A);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_bordering(A,B):return val_func_uppermost(A)==0 or val_func_leftmost(A)==0 or val_func_lowermost(A)==len(B)-1 or val_func_rightmost(A)==len(B[0])-1
def val_func_vmatching(A,B):return len(set(A for(B,A)in val_func_toindices(A))&set(A for(B,A)in val_func_toindices(B)))>0
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
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
def val_func_colorfilter(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def mval_func_apply(A,B):return val_func_merge(val_func_apply(A,B))
def val_func_rbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(D,B)
	elif C==3:return lambda D,E:A(D,E,B)
	else:return lambda D,E,F:A(D,E,F,B)
def val_func_branch(A,B,C):return B if A else C
def val_func_mfilter(A,B):return val_func_merge(val_func_sfilter(A,B))
def val_func_argmin(A,B):return min(A,key=B)
def val_func_argmax(A,B):return max(A,key=B)
def val_func_valmax(A,B):return B(max(A,key=B,default=0))
def val_func_size(A):return len(A)
def val_func_equality(A,B):return A==B
def val_func_multiply(A,B):
	if isinstance(A,int)and isinstance(B,int):return A*B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]*B[0],A[1]*B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A*B[0],A*B[1]
	return A[0]*B,A[1]*B
def p(A):H=False;B=True;A=tuple(map(tuple,A));C=val_func_objects(A,B,H,B);D=val_func_argmin(C,val_func_size);I=val_func_argmax(C,val_func_size);E=val_func_vmatching(D,I);J=val_func_branch(E,(1,0),(0,1));F=val_func_branch(E,val_func_uppermost,val_func_leftmost);K=val_func_valmax(C,F);L=F(D);M=val_func_equality(K,L);N=val_func_branch(M,-1,1);O=val_func_multiply(J,N);P=val_func_inbox(D);Q=val_func_rbind(val_func_shoot,O);R=mval_func_apply(Q,P);G=underval_func_fill(A,8,R);S=val_func_objects(G,B,H,B);T=val_func_colorfilter(S,8);U=val_func_rbind(val_func_bordering,A);V=val_func_mfilter(T,U);W=val_func_cover(G,V);return[*map(list,W)]