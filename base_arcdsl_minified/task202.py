def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_palette(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
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
def val_func_frontiers(A):C,D=len(A),len(A[0]);B=tuple(A for(A,B)in enumerate(A)if len(set(B))==1);E=tuple(A for(A,B)in enumerate(val_func_dmirror(A))if len(set(B))==1);F=frozenset({frozenset({(A[B][C],(B,C))for C in range(D)})for B in B});G=frozenset({frozenset({(A[C][B],(C,B))for C in range(C)})for B in E});return F|G
def val_func_vfrontier(A):return frozenset((B,A[1])for B in range(30))
def val_func_subgrid(A,B):return val_func_crop(B,val_func_ulcorner(A),val_func_shape(A))
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
def val_func_rot90(A):return tuple(A for A in zip(*A[::-1]))
def val_func_color(A):return next(iter(A))[0]
def val_func_hline(A):return val_func_width(A)==len(A)and val_func_height(A)==1
def val_func_partition(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in val_func_palette(A))
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_ofval_func_color(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
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
def val_func_branch(A,B,C):return B if A else C
def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_positive(A):return A>0
def val_func_size(A):return len(A)
def val_func_intersection(A,B):return A&B
def val_func_flip(A):return not A
def val_func_identity(A):return A
def p(A):A=tuple(map(tuple,A));U=val_func_rot90(A);D=val_func_frontiers(A);E=val_func_sfilter(D,val_func_hline);F=val_func_size(E);G=val_func_positive(F);C=val_func_branch(G,val_func_identity,val_func_dmirror);B=C(A);H=val_func_rbind(val_func_subgrid,B);I=val_func_matcher(val_func_color,0);J=val_func_compose(val_func_flip,I);K=val_func_partition(B);L=val_func_sfilter(K,J);M=val_func_rbind(val_func_ofval_func_color,0);N=val_func_lbind(mval_func_apply,val_func_vfrontier);O=val_func_chain(N,M,H);P=val_func_fork(val_func_shift,O,val_func_ulcorner);Q=val_func_fork(val_func_intersection,val_func_toindices,P);R=mval_func_apply(Q,L);S=val_func_fill(B,0,R);T=C(S);return[*map(list,T)]