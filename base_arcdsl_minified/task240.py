def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
def val_func_palette(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_mostval_func_color(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_lefthalf(A):return val_func_rot270(val_func_tophalf(val_func_rot90(A)))
def val_func_tophalf(A):return A[:len(A)//2]
def val_func_cover(A,B):return val_func_fill(A,val_func_mostval_func_color(A),val_func_toindices(B))
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
def val_func_vmirror(A):
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=val_func_ulcorner(A)[1]+val_func_lrcorner(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def val_func_rot270(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def val_func_rot180(A):return tuple(tuple(A[::-1])for A in A[::-1])
def val_func_rot90(A):return tuple(A for A in zip(*A[::-1]))
def val_func_color(A):return next(iter(A))[0]
def val_func_numval_func_colors(A):return len(val_func_palette(A))
def val_func_partition(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in val_func_palette(A))
def val_func_normalize(A):
	if len(A)==0:return A
	return val_func_shift(A,(-val_func_uppermost(A),-val_func_leftmost(A)))
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_reval_func_color(A,B):return frozenset((A,B)for B in val_func_toindices(B))
def val_func_lrcorner(A):return tuple(map(max,zip(*val_func_toindices(A))))
def val_func_llcorner(A):return tuple(map(lambda B:{0:max,1:min}[B[0]](B[1]),enumerate(zip(*val_func_toindices(A)))))
def val_func_urcorner(A):return tuple(map(lambda B:{0:min,1:max}[B[0]](B[1]),enumerate(zip(*val_func_toindices(A)))))
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_sizefilter(A,B):return frozenset(A for A in A if len(A)==B)
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
def val_func_pair(A,B):return tuple(zip(A,B))
def val_func_insert(A,B):return B.union(frozenset({A}))
def val_func_last(A):return max(enumerate(A))[1]
def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_tojvec(A):return 0,A
def val_func_initset(A):return frozenset({A})
def val_func_argmax(A,B):return max(A,key=B)
def val_func_maximum(A):return max(A,default=0)
def val_func_combine(A,B):return type(A)((*A,*B))
def val_func_even(A):return A%2==0
def val_func_add(A,B):
	if isinstance(A,int)and isinstance(B,int):return A+B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]+B[0],A[1]+B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A+B[0],A+B[1]
	return A[0]+B,A[1]+B
def p(A):A=tuple(map(tuple,A));H=val_func_rot90(A);I=val_func_rot180(A);J=val_func_rot270(A);K=val_func_initset(A);L=val_func_chain(val_func_numval_func_colors,val_func_lefthalf,val_func_tophalf);M=val_func_insert(H,K);N=val_func_insert(I,M);O=val_func_insert(J,N);E=val_func_argmax(O,L);P=val_func_vmirror(E);Q=pval_func_apply(val_func_pair,E,P);B=val_func_lbind(val_func_apply,val_func_maximum);F=val_func_apply(B,Q);R=val_func_partition(F);D=val_func_sizefilter(R,4);S=val_func_apply(val_func_llcorner,D);T=val_func_apply(val_func_lrcorner,D);U=val_func_combine(S,T);V=val_func_cover(F,U);W=val_func_tojvec(-2);X=val_func_rbind(val_func_add,(0,2));Y=val_func_rbind(val_func_add,W);G=val_func_compose(X,val_func_ulcorner);Z=val_func_compose(Y,val_func_urcorner);a=val_func_fork(val_func_connect,G,Z);b=val_func_compose(val_func_even,val_func_last);c=val_func_rbind(val_func_sfilter,b);d=val_func_chain(val_func_normalize,c,a);e=val_func_fork(val_func_shift,d,G);f=val_func_fork(val_func_reval_func_color,val_func_color,e);g=mval_func_apply(f,D);C=val_func_paint(V,g);h=val_func_rot90(C);i=val_func_rot180(C);j=val_func_rot270(C);k=pval_func_apply(val_func_pair,C,h);l=val_func_apply(B,k);m=pval_func_apply(val_func_pair,l,i);n=val_func_apply(B,m);o=pval_func_apply(val_func_pair,n,j);p=val_func_apply(B,o);return[*map(list,p)]