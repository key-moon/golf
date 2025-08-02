def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_lrcorner(patch):return tuple(map(max,zip(*val_func_toindices(patch))))
def val_func_ulcorner(patch):return tuple(map(min,zip(*val_func_toindices(patch))))
def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
def val_func_width(piece):
	A=piece
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_height(piece):
	A=piece
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
def val_func_normalize(patch):
	A=patch
	if len(A)==0:return A
	return val_func_shift(A,(-val_func_uppermost(A),-val_func_leftmost(A)))
def val_func_shape(piece):A=piece;return val_func_height(A),val_func_width(A)
def val_func_occurrences(grid,obj):
	A=grid;B=set();J=val_func_normalize(obj);C,D=len(A),len(A[0]);K,L=val_func_shape(obj);M,N=C-K+1,D-L+1
	for E in range(M):
		for F in range(N):
			G=True
			for(O,(H,I))in val_func_shift(J,(E,F)):
				if not(0<=H<C and 0<=I<D and A[H][I]==O):G=False;break
			if G:B.add((E,F))
	return frozenset(B)
def val_func_canvas(value,dimensions):A=dimensions;return tuple(tuple(value for A in range(A[1]))for B in range(A[0]))
def val_func_vconcat(a,b):return a+b
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_dmirror(piece):
	A=piece
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_vmirror(piece):
	A=piece
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=val_func_ulcorner(A)[1]+val_func_lrcorner(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def val_func_hmirror(piece):
	A=piece
	if isinstance(A,tuple):return A[::-1]
	B=val_func_ulcorner(A)[0]+val_func_lrcorner(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def val_func_asobject(grid):return frozenset((D,(A,C))for(A,B)in enumerate(grid)for(C,D)in enumerate(B))
def val_func_shift(patch,directions):
	A=patch
	if len(A)==0:return A
	B,C=directions
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(D+B,E+C))for(A,(D,E))in A)
	return frozenset((A+B,D+C)for(A,D)in A)
def mval_func_apply(function,container):return val_func_merge(val_func_apply(function,container))
def val_func_lbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def val_func_astuple(a,b):return a,b
def p(I):I=tuple(map(tuple,I));O=val_func_canvas(5,(2,2));B=val_func_asobject(O);P=val_func_occurrences(I,B);Q=val_func_lbind(val_func_shift,B);R=mval_func_apply(Q,P);C=val_func_fill(I,8,R);S=val_func_canvas(5,(1,1));T=val_func_astuple(2,1);U=val_func_canvas(8,T);A=val_func_vconcat(U,S);D=val_func_asobject(A);V=val_func_occurrences(C,D);W=val_func_lbind(val_func_shift,D);X=mval_func_apply(W,V);E=val_func_fill(C,2,X);Y=val_func_astuple(1,3);Z=val_func_canvas(5,Y);F=val_func_asobject(Z);a=val_func_occurrences(E,F);b=val_func_lbind(val_func_shift,F);c=mval_func_apply(b,a);G=val_func_fill(E,2,c);d=val_func_hmirror(A);H=val_func_asobject(d);e=val_func_occurrences(G,H);f=val_func_lbind(val_func_shift,H);g=mval_func_apply(f,e);J=val_func_fill(G,2,g);K=val_func_dmirror(A);L=val_func_asobject(K);h=val_func_occurrences(J,L);i=val_func_lbind(val_func_shift,L);j=mval_func_apply(i,h);M=val_func_fill(J,2,j);k=val_func_vmirror(K);N=val_func_asobject(k);l=val_func_occurrences(M,N);m=val_func_lbind(val_func_shift,N);n=mval_func_apply(m,l);o=val_func_fill(M,2,n);return[*map(list,o)]