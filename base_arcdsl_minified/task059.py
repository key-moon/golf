def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_toobject(A,B):D,E=len(B),len(B[0]);return frozenset((B[A][C],(A,C))for(A,C)in val_func_toindices(A)if 0<=A<D and 0<=C<E)
def val_func_colorcount(A,B):
	if isinstance(A,tuple):return sum(A.count(B)for A in A)
	return sum(A==B for(A,C)in A)
def val_func_leastcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_fork(A,B,C):return lambda D:A(B(D),C(D))
def val_func_rbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(D,B)
	elif C==3:return lambda D,E:A(D,E,B)
	else:return lambda D,E,F:A(D,E,F,B)
def val_func_matcher(A,B):return lambda C:A(C)==B
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_product(A,B):return frozenset((C,B)for B in B for C in A)
def val_func_interval(A,B,C):return tuple(range(A,B,C))
def val_func_last(A):return max(enumerate(A))[1]
def val_func_first(A):return next(iter(A))
def val_func_mfilter(A,B):return val_func_merge(val_func_sfilter(A,B))
def val_func_valmax(A,B):return B(max(A,key=B,default=0))
def val_func_flip(A):return not A
def val_func_add(A,B):
	if isinstance(A,int)and isinstance(B,int):return A+B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]+B[0],A[1]+B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A+B[0],A+B[1]
	return A[0]+B,A[1]+B
def val_func_identity(A):return A
def p(A):A=tuple(map(tuple,A));C=val_func_leastcolor(A);D=val_func_interval(0,9,4);H=val_func_product(D,D);I=val_func_rbind(val_func_add,3);J=val_func_rbind(val_func_interval,1);E=val_func_fork(J,val_func_identity,I);K=val_func_compose(E,val_func_first);L=val_func_compose(E,val_func_last);M=val_func_fork(val_func_product,K,L);N=val_func_rbind(val_func_colorcount,C);O=val_func_rbind(val_func_toobject,A);F=val_func_compose(N,O);B=val_func_apply(M,H);P=val_func_valmax(B,F);G=val_func_matcher(F,P);Q=val_func_compose(val_func_flip,G);R=val_func_mfilter(B,G);S=val_func_mfilter(B,Q);T=val_func_fill(A,C,R);U=val_func_fill(T,0,S);return[*map(list,U)]