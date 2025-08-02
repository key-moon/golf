def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def ival_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_dval_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
def val_func_mostcolor(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
def val_func_width(piece):
	A=piece
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
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
def val_func_height(piece):
	A=piece
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def val_func_vperiod(obj):
	A=val_func_normalize(obj);C=val_func_height(A)
	for B in range(1,C):
		D=val_func_shift(A,(-B,0));E=frozenset({(B,(A,C))for(B,(A,C))in D if A>=0})
		if E.issubset(A):return B
def val_func_hperiod(obj):
	A=val_func_normalize(obj);B=val_func_width(A)
	for C in range(1,B):
		D=val_func_shift(A,(0,-C));E=frozenset({(B,(C,A))for(B,(C,A))in D if A>=0})
		if E.issubset(A):return C
	return B
def val_func_canvas(value,dimensions):A=dimensions;return tuple(tuple(value for A in range(A[1]))for B in range(A[0]))
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_paint(grid,obj):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(G,(C,D))in obj:
		if 0<=C<E and 0<=D<F:B[C][D]=G
	return tuple(tuple(A)for A in B)
def val_func_asobject(grid):return frozenset((D,(A,C))for(A,B)in enumerate(grid)for(C,D)in enumerate(B))
def val_func_objects(grid,univalued,diagonal,without_bg):
	A=grid;H=val_func_mostcolor(A)if without_bg else None;I=set();D=set();L,M=len(A),len(A[0]);N=val_func_asindices(A);O=val_func_neighbors if diagonal else val_func_dval_func_neighbors
	for B in N:
		if B in D:continue
		E=A[B[0]][B[1]]
		if E==H:continue
		J={(E,B)};F={B}
		while len(F)>0:
			K=set()
			for C in F:
				G=A[C[0]][C[1]]
				if E==G if univalued else G!=H:J.add((G,C));D.add(C);K|={(A,B)for(A,B)in O(C)if 0<=A<L and 0<=B<M}
			F=K-D
		I.add(frozenset(J))
	return frozenset(I)
def val_func_neighbors(loc):return val_func_dval_func_neighbors(loc)|ival_func_neighbors(loc)
def val_func_shift(patch,directions):
	A=patch
	if len(A)==0:return A
	B,C=directions
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(D+B,E+C))for(A,(D,E))in A)
	return frozenset((A+B,D+C)for(A,D)in A)
def val_func_shape(piece):A=piece;return val_func_height(A),val_func_width(A)
def mval_func_apply(function,container):return val_func_merge(val_func_apply(function,container))
def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_power(function,n):
	A=function
	if n==1:return A
	return val_func_compose(A,val_func_power(A,n-1))
def val_func_lbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def val_func_astuple(a,b):return a,b
def val_func_first(container):return next(iter(container))
def val_func_decrement(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def val_func_double(n):return n*2 if isinstance(n,int)else(n[0]*2,n[1]*2)
def val_func_multiply(a,b):
	if isinstance(a,int)and isinstance(b,int):return a*b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]*b[0],a[1]*b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a*b[0],a*b[1]
	return a[0]*b,a[1]*b
def p(I):C=False;I=tuple(map(tuple,I));D=val_func_asobject(I);B=val_func_shape(I);E=val_func_decrement(B);F=val_func_index(I,E);G=val_func_double(B);H=val_func_canvas(F,G);J=val_func_paint(H,D);K=val_func_objects(J,C,C,True);L=val_func_first(K);A=val_func_shift(L,(0,-1));M=val_func_vperiod(A);N=val_func_hperiod(A);O=val_func_neighbors((0,0));P=val_func_lbind(mval_func_apply,val_func_neighbors);Q=val_func_power(P,2);R=Q(O);S=val_func_astuple(M,N);T=val_func_lbind(val_func_multiply,S);U=val_func_apply(T,R);V=val_func_lbind(val_func_shift,A);W=mval_func_apply(V,U);X=val_func_paint(I,W);return[*map(list,X)]