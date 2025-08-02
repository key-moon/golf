def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_ival_func_neighbors(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(A):return val_func_dval_func_neighbors(A)|val_func_ival_func_neighbors(A)
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def val_func_mostcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
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
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_toobject(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in val_func_toindices(A)if 0<=A<D and 0<=C<E)
def val_func_hline(A):return val_func_width(A)==len(A)and val_func_height(A)==1
def val_func_vline(A):return val_func_height(A)==len(A)and val_func_width(A)==1
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
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_colorfilter(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def val_func_colorcount(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def prval_func_apply(A,B,C):return frozenset(A(D,C)for C in C for D in B)
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
def val_func_insert(A,B):return B.union(frozenset({A}))
def val_func_mfilter(A,B):return val_func_merge(val_func_sfilter(A,B))
def val_func_tojvec(A):return 0,A
def val_func_toivec(A):return A,0
def val_func_either(A,B):return A or B
def val_func_both(A,B):return A and B
def val_func_initset(A):return frozenset({A})
def val_func_argmax(A,B):return max(A,key=B)
def val_func_valmax(A,B):return B(max(A,key=B,default=0))
def val_func_size(A):return len(A)
def val_func_greater(A,B):return A>B
def val_func_combine(A,B):return type(A)((*A,*B))
def val_func_halve(A):return A//2 if isinstance(A,int)else(A[0]//2,A[1]//2)
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
def p(A):H=False;A=tuple(map(tuple,A));B=val_func_ofcolor(A,2);I=prval_func_apply(val_func_connect,B,B);J=val_func_lbind(val_func_greater,6);K=val_func_compose(J,val_func_size);L=val_func_fork(val_func_either,val_func_vline,val_func_hline);M=val_func_fork(val_func_both,K,L);N=val_func_mfilter(I,M);C=val_func_fill(A,2,N);O=val_func_objects(C,True,H,H);D=val_func_colorfilter(O,2);P=val_func_valmax(D,val_func_width);E=val_func_halve(P);F=val_func_toivec(E);G=val_func_tojvec(E);Q=val_func_rbind(val_func_add,(0,2));R=val_func_rbind(val_func_add,(2,0));S=val_func_rbind(val_func_subtract,(0,2));T=val_func_rbind(val_func_subtract,(2,0));U=val_func_rbind(val_func_colorcount,2);V=val_func_rbind(val_func_toobject,C);W=val_func_compose(val_func_initset,Q);X=val_func_fork(val_func_insert,R,W);Y=val_func_fork(val_func_insert,S,X);Z=val_func_fork(val_func_insert,T,Y);a=val_func_fork(val_func_combine,val_func_dval_func_neighbors,Z);b=val_func_chain(U,V,a);c=val_func_rbind(val_func_argmax,b);d=val_func_compose(c,val_func_toindices);e=val_func_apply(d,D);f=val_func_rbind(val_func_add,F);g=val_func_rbind(val_func_subtract,F);h=val_func_rbind(val_func_add,G);i=val_func_rbind(val_func_subtract,G);j=val_func_fork(val_func_connect,f,g);k=val_func_fork(val_func_connect,h,i);l=val_func_fork(val_func_combine,j,k);m=mval_func_apply(l,e);n=val_func_fill(C,8,m);o=val_func_fill(n,2,B);return[*map(list,o)]