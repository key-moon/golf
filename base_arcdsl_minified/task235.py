def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_crop(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def val_func_canvas(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def val_func_hsplit(A,B):D,C=len(A),len(A[0])//B;E=len(A[0])%B!=0;return tuple(val_func_crop(A,(0,C*B+B*E),(D,C))for B in range(B))
def val_func_hupscale(A,B):
	C=tuple()
	for E in A:
		D=tuple()
		for F in E:D=D+tuple(F for A in range(B))
		C=C+(D,)
	return C
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_fork(A,B,C):return lambda D:A(B(D),C(D))
def val_func_power(A,B):
	if B==1:return A
	return val_func_compose(A,val_func_power(A,B-1))
def val_func_rbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(D,B)
	elif C==3:return lambda D,E:A(D,E,B)
	else:return lambda D,E,F:A(D,E,F,B)
def val_func_matcher(A,B):return lambda C:A(C)==B
def val_func_chain(A,B,C):return lambda D:A(B(C(D)))
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_astuple(A,B):return A,B
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_size(A):return len(A)
def val_func_double(A):return A*2 if isinstance(A,int)else(A[0]*2,A[1]*2)
def val_func_multiply(A,B):
	if isinstance(A,int)and isinstance(B,int):return A*B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]*B[0],A[1]*B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A*B[0],A*B[1]
	return A[0]*B,A[1]*B
def val_func_add(A,B):
	if isinstance(A,int)and isinstance(B,int):return A+B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]+B[0],A[1]+B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A+B[0],A+B[1]
	return A[0]+B,A[1]+B
def p(A):A=tuple(map(tuple,A));E=val_func_hsplit(A,3);F=val_func_astuple(2,1);C=val_func_rbind(val_func_ofcolor,0);B=val_func_compose(val_func_ulcorner,C);G=val_func_compose(val_func_size,C);H=val_func_matcher(G,0);I=val_func_matcher(B,(1,1));J=val_func_matcher(B,(1,0));K=val_func_matcher(B,F);L=val_func_rbind(val_func_multiply,3);D=val_func_power(val_func_double,2);M=val_func_compose(val_func_double,H);N=val_func_chain(D,val_func_double,I);O=val_func_compose(L,J);P=val_func_compose(D,K);Q=val_func_fork(val_func_add,M,N);R=val_func_fork(val_func_add,O,P);S=val_func_fork(val_func_add,Q,R);T=val_func_rbind(val_func_canvas,(1,1));U=val_func_compose(T,S);V=val_func_apply(U,E);W=val_func_merge(V);X=val_func_hupscale(W,3);return[*map(list,X)]