def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
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
def val_func_connect(A,B):
	C,D=A;E,F=B;G=min(C,E);H=max(C,E)+1;I=min(D,F);J=max(D,F)+1
	if C==E:return frozenset((C,A)for A in range(I,J))
	elif D==F:return frozenset((A,D)for A in range(G,H))
	elif E-C==F-D:return frozenset((A,B)for(A,B)in zip(range(G,H),range(I,J)))
	elif E-C==D-F:return frozenset((A,B)for(A,B)in zip(range(G,H),range(J-1,I-1,-1)))
	return frozenset()
def val_func_shoot(A,B):return val_func_connect(A,(A[0]+42*B[0],A[1]+42*B[1]))
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_dmirror(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
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
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_portrait(A):return val_func_height(A)>val_func_width(A)
def val_func_height(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def pval_func_apply(A,B,C):return tuple(A(B,C)for(B,C)in zip(B,C))
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
def val_func_branch(A,B,C):return B if A else C
def val_func_pair(A,B):return tuple(zip(A,B))
def val_func_astuple(A,B):return A,B
def val_func_interval(A,B,C):return tuple(range(A,B,C))
def val_func_insert(A,B):return B.union(frozenset({A}))
def val_func_last(A):return max(enumerate(A))[1]
def val_func_first(A):return next(iter(A))
def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_tojvec(A):return 0,A
def val_func_decrement(A):return A-1 if isinstance(A,int)else(A[0]-1,A[1]-1)
def val_func_increment(A):return A+1 if isinstance(A,int)else(A[0]+1,A[1]+1)
def val_func_both(A,B):return A and B
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_size(A):return len(A)
def val_func_greater(A,B):return A>B
def val_func_order(A,B):return tuple(sorted(A,key=B))
def val_func_equality(A,B):return A==B
def val_func_identity(A):return A
def p(A):A=tuple(map(tuple,A));C=val_func_ofcolor(A,2);K=val_func_portrait(C);D=val_func_branch(K,val_func_identity,val_func_dmirror);L=D(A);M=val_func_leftmost(C);N=val_func_equality(M,0);E=val_func_branch(N,val_func_identity,val_func_vmirror);F=E(L);O=val_func_ofcolor(F,8);P=val_func_uppermost(O);Q=val_func_equality(P,0);G=val_func_branch(Q,val_func_identity,val_func_hmirror);B=G(F);R=val_func_ofcolor(B,8);H=val_func_ofcolor(B,2);S=val_func_rbind(val_func_shoot,(1,0));T=mval_func_apply(S,R);U=val_func_height(B);I=val_func_apply(val_func_first,H);V=val_func_insert(0,I);W=val_func_insert(U,I);X=val_func_apply(val_func_decrement,W);Y=val_func_order(V,val_func_identity);Z=val_func_order(X,val_func_identity);a=val_func_size(H);b=val_func_increment(a);c=val_func_interval(0,b,1);d=val_func_apply(val_func_tojvec,c);e=val_func_pair(Y,Z);f=val_func_lbind(val_func_sfilter,T);J=val_func_compose(val_func_first,val_func_last);g=val_func_chain(val_func_decrement,val_func_first,val_func_first);h=val_func_fork(val_func_greater,J,g);i=val_func_chain(val_func_increment,val_func_last,val_func_first);j=val_func_fork(val_func_greater,i,J);k=val_func_fork(val_func_both,h,j);l=val_func_lbind(val_func_lbind,val_func_astuple);m=val_func_lbind(val_func_compose,k);n=val_func_chain(f,m,l);o=val_func_apply(n,e);p=pval_func_apply(val_func_shift,o,d);q=val_func_merge(p);r=val_func_fill(B,8,q);s=val_func_chain(D,E,G);t=s(r);return[*map(list,t)]