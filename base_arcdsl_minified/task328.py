def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_ival_func_neighbors(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(A):return val_func_dval_func_neighbors(A)|val_func_ival_func_neighbors(A)
def val_func_dval_func_neighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_mostval_func_color(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
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
def val_func_paint(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
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
def reval_func_color(A,B):return frozenset((A,B)for B in val_func_toindices(B))
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def mval_func_apply(A,B):return val_func_merge(val_func_apply(A,B))
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
def val_func_chain(A,B,C):return lambda D:A(B(C(D)))
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_astuple(A,B):return A,B
def val_func_remove(A,B):return type(B)(B for B in B if B!=A)
def val_func_last(A):return max(enumerate(A))[1]
def val_func_first(A):return next(iter(A))
def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_sign(A):
	if isinstance(A,int):return 0 if A==0 else 1 if A>0 else-1
	return 0 if A[0]==0 else 1 if A[0]>0 else-1,0 if A[1]==0 else 1 if A[1]>0 else-1
def val_func_argmin(A,B):return min(A,key=B)
def val_func_valmin(A,B):return B(min(A,key=B,default=0))
def val_func_maximum(A):return max(A,default=0)
def val_func_greater(A,B):return A>B
def val_func_intersection(A,B):return A&B
def val_func_equality(A,B):return A==B
def val_func_even(A):return A%2==0
def val_func_multiply(A,B):
	if isinstance(A,int)and isinstance(B,int):return A*B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]*B[0],A[1]*B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A*B[0],A*B[1]
	return A[0]*B,A[1]*B
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
def p(A):A=tuple(map(tuple,A));I=val_func_asindices(A);B=val_func_objects(A,True,False,True);J=val_func_fork(val_func_multiply,val_func_sign,val_func_identity);D=val_func_lbind(val_func_apply,J);K=val_func_chain(val_func_even,val_func_maximum,D);C=val_func_lbind(val_func_sfilter,I);L=val_func_fork(val_func_add,val_func_first,val_func_last);M=val_func_rbind(val_func_remove,B);N=val_func_compose(val_func_center,val_func_last);E=val_func_fork(val_func_subtract,val_func_first,N);O=val_func_compose(K,E);P=val_func_lbind(val_func_rbind,val_func_equality);Q=val_func_lbind(val_func_argmin,B);R=val_func_chain(L,D,E);S=val_func_lbind(val_func_lbind,val_func_astuple);F=val_func_lbind(val_func_rbind,val_func_astuple);T=val_func_lbind(val_func_compose,O);G=val_func_lbind(val_func_compose,R);H=val_func_compose(G,S);U=val_func_compose(G,F);V=val_func_compose(Q,H);W=val_func_rbind(val_func_compose,V);X=val_func_lbind(val_func_lbind,val_func_valmin);Y=val_func_rbind(val_func_compose,H);Z=val_func_chain(Y,X,M);a=val_func_lbind(val_func_fork,val_func_greater);b=val_func_fork(a,Z,U);c=val_func_chain(C,T,F);d=val_func_chain(C,W,P);e=val_func_fork(val_func_intersection,c,d);f=val_func_compose(C,b);g=val_func_fork(val_func_intersection,e,f);h=val_func_fork(reval_func_color,val_func_color,g);i=mval_func_apply(h,B);j=val_func_paint(A,i);return[*map(list,j)]