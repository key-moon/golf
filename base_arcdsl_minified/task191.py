def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_crop(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def val_func_shape(A):return val_func_height(A),val_func_width(A)
def val_func_subgrid(A,B):return val_func_crop(B,val_func_ulcorner(A),val_func_shape(A))
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_rot270(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def val_func_rot180(A):return tuple(tuple(A[::-1])for A in A[::-1])
def val_func_rot90(A):return tuple(A for A in zip(*A[::-1]))
def val_func_normalize(A):
	if len(A)==0:return A
	return val_func_shift(A,(-val_func_uppermost(A),-val_func_leftmost(A)))
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_height(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def mpval_func_apply(A,B,C):return val_func_merge(pval_func_apply(A,B,C))
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
def val_func_matcher(A,B):return lambda C:A(C)==B
def val_func_chain(A,B,C):return lambda D:A(B(C(D)))
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_product(A,B):return frozenset((C,B)for B in B for C in A)
def val_func_astuple(A,B):return A,B
def val_func_interval(A,B,C):return tuple(range(A,B,C))
def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_increment(A):return A+1 if isinstance(A,int)else(A[0]+1,A[1]+1)
def val_func_size(A):return len(A)
def val_func_difference(A,B):return type(A)(A for A in A if A not in B)
def val_func_combine(A,B):return type(A)((*A,*B))
def val_func_subtract(A,B):
	if isinstance(A,int)and isinstance(B,int):return A-B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]-B[0],A[1]-B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A-B[0],A-B[1]
	return A[0]-B,A[1]-B
def p(A):A=tuple(map(tuple,A));I=val_func_height(A);J=val_func_width(A);C=val_func_ofcolor(A,1);K=val_func_ofcolor(A,4);L=val_func_ulcorner(C);B=val_func_subgrid(C,A);M=val_func_rot90(B);N=val_func_rot180(B);O=val_func_rot270(B);P=val_func_matcher(val_func_size,0);Q=val_func_rbind(val_func_ofcolor,1);R=val_func_compose(val_func_normalize,Q);S=val_func_rbind(val_func_ofcolor,4);T=val_func_rbind(val_func_shift,L);U=val_func_compose(T,S);V=val_func_lbind(val_func_subtract,I);W=val_func_chain(val_func_increment,V,val_func_height);X=val_func_lbind(val_func_subtract,J);Y=val_func_chain(val_func_increment,X,val_func_width);Z=val_func_rbind(val_func_interval,1);D=val_func_lbind(Z,0);a=val_func_compose(D,W);b=val_func_compose(D,Y);c=val_func_fork(val_func_product,a,b);d=val_func_rbind(val_func_shift,(-1,-1));E=val_func_lbind(val_func_lbind,val_func_shift);e=val_func_chain(E,d,R);f=val_func_astuple(B,M);g=val_func_astuple(N,O);F=val_func_combine(f,g);G=val_func_apply(U,F);h=val_func_lbind(val_func_difference,K);i=val_func_apply(h,G);H=val_func_apply(val_func_normalize,G);j=val_func_apply(c,H);k=val_func_lbind(val_func_rbind,val_func_difference);l=val_func_apply(E,H);m=val_func_apply(k,i);n=pval_func_apply(val_func_compose,m,l);o=val_func_lbind(val_func_compose,P);p=val_func_apply(o,n);q=pval_func_apply(val_func_sfilter,j,p);r=val_func_apply(e,F);s=mpval_func_apply(mval_func_apply,r,q);t=val_func_fill(A,1,s);return[*map(list,t)]