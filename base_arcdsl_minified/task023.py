def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_lrcorner(A):return tuple(map(max,zip(*val_func_toindices(A))))
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
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
def val_func_vconcat(A,B):return A+B
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
def val_func_asobject(A):return frozenset((D,(A,C))for(A,B)in enumerate(A)for(C,D)in enumerate(B))
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def mval_func_apply(A,B):return val_func_merge(val_func_apply(A,B))
def val_func_lbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(B,D)
	elif C==3:return lambda D,E:A(B,D,E)
	else:return lambda D,E,F:A(B,D,E,F)
def val_func_astuple(A,B):return A,B
def p(A):A=tuple(map(tuple,A));O=val_func_canvas(5,(2,2));C=val_func_asobject(O);P=val_func_occurrences(A,C);Q=val_func_lbind(val_func_shift,C);R=mval_func_apply(Q,P);D=val_func_fill(A,8,R);S=val_func_canvas(5,(1,1));T=val_func_astuple(2,1);U=val_func_canvas(8,T);B=val_func_vconcat(U,S);E=val_func_asobject(B);V=val_func_occurrences(D,E);W=val_func_lbind(val_func_shift,E);X=mval_func_apply(W,V);F=val_func_fill(D,2,X);Y=val_func_astuple(1,3);Z=val_func_canvas(5,Y);G=val_func_asobject(Z);a=val_func_occurrences(F,G);b=val_func_lbind(val_func_shift,G);c=mval_func_apply(b,a);H=val_func_fill(F,2,c);d=val_func_hmirror(B);I=val_func_asobject(d);e=val_func_occurrences(H,I);f=val_func_lbind(val_func_shift,I);g=mval_func_apply(f,e);J=val_func_fill(H,2,g);K=val_func_dmirror(B);L=val_func_asobject(K);h=val_func_occurrences(J,L);i=val_func_lbind(val_func_shift,L);j=mval_func_apply(i,h);M=val_func_fill(J,2,j);k=val_func_vmirror(K);N=val_func_asobject(k);l=val_func_occurrences(M,N);m=val_func_lbind(val_func_shift,N);n=mval_func_apply(m,l);o=val_func_fill(M,2,n);return[*map(list,o)]