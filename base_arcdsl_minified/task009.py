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
def val_func_paint(A,B):
	F,G=len(A),len(A[0]);C=list(list(A)for A in A)
	for(H,(D,E))in B:
		if 0<=D<F and 0<=E<G:C[D][E]=H
	return tuple(tuple(A)for A in C)
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_color(A):return next(iter(A))[0]
def val_func_hline(A):return val_func_width(A)==len(A)and val_func_height(A)==1
def val_func_vline(A):return val_func_height(A)==len(A)and val_func_width(A)==1
def val_func_partition(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in val_func_palette(A))
def reval_func_color(A,B):return frozenset((A,B)for B in val_func_toindices(B))
def val_func_ofval_func_color(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_val_func_colorfilter(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def val_func_mostval_func_color(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_fork(A,B,C):return lambda D:A(B(D),C(D))
def val_func_power(A,B):
	if B==1:return A
	return val_func_compose(A,val_func_power(A,B-1))
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_product(A,B):return frozenset((C,B)for B in B for C in A)
def val_func_remove(A,B):return type(B)(B for B in B if B!=A)
def val_func_last(A):return max(enumerate(A))[1]
def val_func_first(A):return next(iter(A))
def val_func_mfilter(A,B):return val_func_merge(val_func_sfilter(A,B))
def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_either(A,B):return A or B
def val_func_argmax(A,B):return max(A,key=B)
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_size(A):return len(A)
def val_func_difference(A,B):return type(A)(A for A in A if A not in B)
def val_func_equality(A,B):return A==B
def p(A):A=tuple(map(tuple,A));B=val_func_partition(A);C=val_func_mostval_func_color(A);E=val_func_ofval_func_color(A,C);F=val_func_val_func_colorfilter(B,0);G=val_func_argmax(B,val_func_size);H=val_func_difference(B,F);I=val_func_remove(G,H);D=val_func_merge(I);J=val_func_product(D,D);K=val_func_power(val_func_first,2);L=val_func_compose(val_func_first,val_func_last);M=val_func_fork(val_func_equality,K,L);N=val_func_sfilter(J,M);O=val_func_compose(val_func_last,val_func_first);P=val_func_power(val_func_last,2);Q=val_func_fork(val_func_connect,O,P);R=val_func_fork(reval_func_color,val_func_color,Q);S=val_func_apply(R,N);T=val_func_fork(val_func_either,val_func_vline,val_func_hline);U=val_func_mfilter(S,T);V=val_func_paint(A,U);W=val_func_fill(V,C,E);return[*map(list,W)]