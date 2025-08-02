def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_ival_func_neighbors(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(A):return val_func_dval_func_neighbors(A)|val_func_ival_func_neighbors(A)
def val_func_dval_func_neighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def val_func_manhattan(A,B):return min(abs(A-D)+abs(C-E)for(A,C)in val_func_toindices(A)for(D,E)in val_func_toindices(B))
def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
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
def val_func_lrcorner(A):return tuple(map(max,zip(*val_func_toindices(A))))
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_backdrop(A):
	if len(A)==0:return frozenset({})
	B=val_func_toindices(A);C,D=val_func_ulcorner(B);E,F=val_func_lrcorner(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
def val_func_delta(A):
	if len(A)==0:return frozenset({})
	return val_func_backdrop(A)-val_func_toindices(A)
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_position(A,B):
	C,D=val_func_center(val_func_toindices(A));E,F=val_func_center(val_func_toindices(B))
	if C==E:return 0,1 if D<F else-1
	elif D==F:return 1 if C<E else-1,0
	elif C<E:return 1,1 if D<F else-1
	elif C>E:return-1,1 if D<F else-1
def val_func_paint(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
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
def val_func_adjacent(A,B):return val_func_manhattan(A,B)==1
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
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_shape(A):return val_func_height(A),val_func_width(A)
def val_func_mostcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
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
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_insert(A,B):return B.union(frozenset({A}))
def val_func_last(A):return max(enumerate(A))[1]
def val_func_first(A):return next(iter(A))
def val_func_extract(A,B):return next(A for A in A if B(A))
def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_tojvec(A):return 0,A
def val_func_toivec(A):return A,0
def val_func_crement(A):
	if isinstance(A,int):return 0 if A==0 else A+1 if A>0 else A-1
	return 0 if A[0]==0 else A[0]+1 if A[0]>0 else A[0]-1,0 if A[1]==0 else A[1]+1 if A[1]>0 else A[1]-1
def val_func_initset(A):return frozenset({A})
def val_func_difference(A,B):return type(A)(A for A in A if A not in B)
def val_func_intersection(A,B):return A&B
def val_func_combine(A,B):return type(A)((*A,*B))
def val_func_equality(A,B):return A==B
def val_func_invert(A):return-A if isinstance(A,int)else(-A[0],-A[1])
def val_func_multiply(A,B):
	if isinstance(A,int)and isinstance(B,int):return A*B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]*B[0],A[1]*B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A*B[0],A*B[1]
	return A[0]*B,A[1]*B
def val_func_identity(A):return A
def p(A):A=tuple(map(tuple,A));E=val_func_objects(A,False,True,True);Q=val_func_lbind(val_func_rbind,val_func_equality);R=val_func_rbind(val_func_compose,val_func_first);S=val_func_chain(R,Q,val_func_mostcolor);B=val_func_fork(val_func_sfilter,val_func_identity,S);F=val_func_fork(val_func_difference,val_func_identity,B);T=val_func_lbind(val_func_rbind,val_func_adjacent);U=val_func_rbind(val_func_compose,val_func_initset);V=val_func_chain(U,T,F);W=val_func_fork(val_func_extract,B,V);K=val_func_fork(val_func_insert,W,F);X=val_func_lbind(val_func_recolor,0);Y=val_func_chain(X,val_func_delta,K);Z=val_func_fork(val_func_combine,K,Y);C=val_func_fork(val_func_position,B,F);L=val_func_chain(val_func_toivec,val_func_first,C);M=val_func_chain(val_func_tojvec,val_func_last,C);a=val_func_fork(val_func_multiply,val_func_shape,L);b=val_func_fork(val_func_multiply,val_func_shape,M);c=val_func_fork(val_func_multiply,val_func_shape,C);d=val_func_fork(val_func_shift,val_func_hmirror,a);e=val_func_fork(val_func_shift,val_func_vmirror,b);f=val_func_compose(val_func_hmirror,val_func_vmirror);g=val_func_fork(val_func_shift,f,c);G=val_func_lbind(val_func_compose,B);h=G(d);i=G(e);j=G(g);k=val_func_compose(val_func_crement,val_func_invert);H=val_func_lbind(val_func_compose,k);l=H(L);m=H(M);n=H(C);N=val_func_fork(val_func_shift,h,l);O=val_func_fork(val_func_shift,i,m);P=val_func_fork(val_func_shift,j,n);I=val_func_lbind(val_func_index,A);D=val_func_lbind(val_func_compose,val_func_toindices);J=D(Z);o=D(N);p=D(O);q=D(P);r=val_func_fork(val_func_intersection,J,o);s=val_func_fork(val_func_intersection,J,p);t=val_func_fork(val_func_intersection,J,q);u=val_func_chain(I,val_func_first,r);v=val_func_chain(I,val_func_first,s);w=val_func_chain(I,val_func_first,t);x=val_func_fork(val_func_recolor,u,N);y=val_func_fork(val_func_recolor,v,O);z=val_func_fork(val_func_recolor,w,P);À=mval_func_apply(x,E);Á=mval_func_apply(y,E);Â=mval_func_apply(z,E);Ã=val_func_paint(A,À);Ä=val_func_paint(Ã,Á);Å=val_func_paint(Ä,Â);return[*map(list,Å)]