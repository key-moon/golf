def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_ival_func_neighbors(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_height(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
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
def val_func_normalize(A):
	if len(A)==0:return A
	return val_func_shift(A,(-val_func_uppermost(A),-val_func_leftmost(A)))
def val_func_shape(A):return val_func_height(A),val_func_width(A)
def val_func_occurrences(A,B):
	C=set();K=val_func_normalize(B);D,E=len(A),len(A[0]);L,M=val_func_shape(B);N,O=D-L+1,E-M+1
	for F in range(N):
		for G in range(O):
			H=True
			for(P,(I,J))in val_func_shift(K,(F,G)):
				if not(0<=I<D and 0<=J<E and A[I][J]==P):H=False;break
			if H:C.add((F,G))
	return frozenset(C)
def val_func_canvas(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_asobject(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def val_func_toobject(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in val_func_toindices(A)if 0<=A<D and 0<=C<E)
def val_func_palette(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_bordering(A,B):return val_func_uppermost(A)==0 or val_func_leftmost(A)==0 or val_func_lowermost(A)==len(B)-1 or val_func_rightmost(A)==len(B[0])-1
def val_func_neighbors(A):return val_func_dval_func_neighbors(A)|val_func_ival_func_neighbors(A)
def val_func_dval_func_neighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def val_func_colorcount(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
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
def val_func_matcher(A,B):return lambda C:A(C)==B
def val_func_chain(A,B,C):return lambda D:A(B(C(D)))
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_product(A,B):return frozenset((C,B)for B in B for C in A)
def val_func_astuple(A,B):return A,B
def val_func_interval(A,B,C):return tuple(range(A,B,C))
def val_func_last(A):return max(enumerate(A))[1]
def val_func_first(A):return next(iter(A))
def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_positive(A):return A>0
def val_func_both(A,B):return A and B
def val_func_initset(A):return frozenset({A})
def val_func_argmax(A,B):return max(A,key=B)
def val_func_size(A):return len(A)
def val_func_contained(A,B):return A in B
def val_func_multiply(A,B):
	if isinstance(A,int)and isinstance(B,int):return A*B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]*B[0],A[1]*B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A*B[0],A*B[1]
	return A[0]*B,A[1]*B
def val_func_identity(A):return A
def p(A):A=tuple(map(tuple,A));I=val_func_asindices(A);J=val_func_fork(val_func_product,val_func_identity,val_func_identity);K=val_func_lbind(val_func_canvas,0);C=val_func_compose(val_func_asobject,K);L=val_func_fork(val_func_multiply,val_func_first,val_func_last);M=val_func_compose(val_func_positive,val_func_size);N=val_func_lbind(val_func_lbind,val_func_shift);O=val_func_rbind(val_func_fork,L);P=val_func_lbind(O,val_func_multiply);Q=val_func_lbind(val_func_chain,M);R=val_func_rbind(Q,C);S=val_func_lbind(val_func_lbind,val_func_occurrences);T=val_func_chain(P,R,S);U=val_func_compose(J,val_func_first);V=val_func_compose(T,val_func_last);E=val_func_fork(val_func_argmax,U,V);W=val_func_chain(N,C,E);X=val_func_compose(C,E);Y=val_func_fork(val_func_occurrences,val_func_last,X);D=val_func_fork(mval_func_apply,W,Y);Z=val_func_multiply(2,6);a=val_func_interval(3,Z,1);b=val_func_astuple(a,A);c=D(b);F=val_func_fill(A,3,c);G=val_func_interval(3,10,1);d=val_func_astuple(G,F);e=D(d);H=val_func_fill(F,3,e);f=val_func_astuple(G,H);g=D(f);h=val_func_fill(H,3,g);i=val_func_rbind(val_func_toobject,h);j=val_func_rbind(val_func_colorcount,3);k=val_func_chain(j,i,val_func_neighbors);l=val_func_matcher(k,8);m=val_func_sfilter(I,l);B=val_func_fill(A,3,m);n=val_func_ofcolor(B,0);o=val_func_rbind(val_func_bordering,B);p=val_func_compose(o,val_func_initset);q=val_func_lbind(val_func_contained,3);r=val_func_rbind(val_func_toobject,B);s=val_func_chain(q,val_func_palette,r);t=val_func_compose(s,val_func_dval_func_neighbors);u=val_func_fork(val_func_both,t,p);v=val_func_sfilter(n,u);w=val_func_fill(B,3,v);return[*map(list,w)]