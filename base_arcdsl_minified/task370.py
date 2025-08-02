def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
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
def val_func_position(A,B):
	C,D=val_func_center(val_func_toindices(A));E,F=val_func_center(val_func_toindices(B))
	if C==E:return 0,1 if D<F else-1
	elif D==F:return 1 if C<E else-1,0
	elif C<E:return 1,1 if D<F else-1
	elif C>E:return-1,1 if D<F else-1
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_lrcorner(A):return tuple(map(max,zip(*val_func_toindices(A))))
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_shape(A):return val_func_height(A),val_func_width(A)
def val_func_leastcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def mval_func_apply(A,B):return val_func_merge(val_func_apply(A,B))
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_fork(A,B,C):return lambda D:A(B(D),C(D))
def val_func_lbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(B,D)
	elif C==3:return lambda D,E:A(B,D,E)
	else:return lambda D,E,F:A(B,D,E,F)
def val_func_branch(A,B,C):return B if A else C
def val_func_interval(A,B,C):return tuple(range(A,B,C))
def val_func_crement(A):
	if isinstance(A,int):return 0 if A==0 else A+1 if A>0 else A-1
	return 0 if A[0]==0 else A[0]+1 if A[0]>0 else A[0]-1,0 if A[1]==0 else A[1]+1 if A[1]>0 else A[1]-1
def val_func_intersection(A,B):return A&B
def val_func_equality(A,B):return A==B
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
def p(A):A=tuple(map(tuple,A));C=val_func_leastcolor(A);B=val_func_ofcolor(A,0);E=val_func_ofcolor(A,C);F=val_func_position(B,E);G=val_func_fork(val_func_connect,val_func_ulcorner,val_func_lrcorner);D=G(B);H=val_func_intersection(B,D);I=val_func_equality(D,H);J=val_func_fork(val_func_subtract,val_func_identity,val_func_crement);K=val_func_fork(val_func_add,val_func_identity,J);L=val_func_branch(I,val_func_identity,K);M=val_func_shape(B);N=val_func_multiply(M,F);O=val_func_apply(L,N);P=val_func_interval(1,5,1);Q=val_func_lbind(val_func_multiply,O);R=val_func_apply(Q,P);S=val_func_lbind(val_func_shift,B);T=mval_func_apply(S,R);U=val_func_fill(A,C,T);return[*map(list,U)]