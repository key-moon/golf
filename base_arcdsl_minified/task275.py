def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
def val_func_height(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def val_func_palette(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_crop(A,B,C):return tuple(A[B[1]:B[1]+C[1]]for A in A[B[0]:B[0]+C[0]])
def val_func_vsplit(A,B):C,D=len(A)//B,len(A[0]);E=len(A)%B!=0;return tuple(val_func_crop(A,(C*B+B*E,0),(C,D))for B in range(B))
def val_func_hsplit(A,B):D,C=len(A),len(A[0])//B;E=len(A[0])%B!=0;return tuple(val_func_crop(A,(0,C*B+B*E),(D,C))for B in range(B))
def val_func_upscale(A,B):
	if isinstance(A,tuple):
		C=tuple()
		for I in A:
			D=tuple()
			for E in I:D=D+tuple(E for A in range(B))
			C=C+tuple(D for A in range(B))
		return C
	else:
		if len(A)==0:return frozenset()
		F,G=val_func_ulcorner(A);J,K=-F,-G;L=val_func_shift(A,(J,K));H=set()
		for(E,(M,N))in L:
			for O in range(B):
				for P in range(B):H.add((E,(M*B+O,N*B+P)))
		return val_func_shift(frozenset(H),(F,G))
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
def val_func_numcolors(A):return len(val_func_palette(A))
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_portrait(A):return val_func_height(A)>val_func_width(A)
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_rbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(D,B)
	elif C==3:return lambda D,E:A(D,E,B)
	else:return lambda D,E,F:A(D,E,F,B)
def val_func_chain(A,B,C):return lambda D:A(B(C(D)))
def val_func_branch(A,B,C):return B if A else C
def val_func_argmin(A,B):return min(A,key=B)
def val_func_argmax(A,B):return max(A,key=B)
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_repeat(A,B):return tuple(A for B in range(B))
def p(A):A=tuple(map(tuple,A));F=val_func_portrait(A);G=val_func_branch(F,val_func_vsplit,val_func_hsplit);B=G(A,2);H=val_func_argmin(B,val_func_numcolors);C=val_func_argmax(B,val_func_numcolors);D=val_func_width(C);I=val_func_rbind(val_func_repeat,D);E=val_func_chain(val_func_dmirror,val_func_merge,I);J=val_func_upscale(C,D);K=E(H);L=E(K);M=val_func_ofcolor(L,0);N=val_func_fill(J,0,M);return[*map(list,N)]