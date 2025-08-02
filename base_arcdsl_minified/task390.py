def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
def ival_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(loc):return val_func_dval_func_neighbors(loc)|ival_func_neighbors(loc)
def val_func_dval_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
def val_func_mostcolor(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_lrcorner(patch):return tuple(map(max,zip(*val_func_toindices(patch))))
def val_func_shape(piece):A=piece;return val_func_height(A),val_func_width(A)
def val_func_crop(grid,start,dims):A=start;return tuple(B[A[1]:A[1]+dims[1]]for B in grid[A[0]:A[0]+dims[0]])
def val_func_trim(grid):return tuple(A[1:-1]for A in grid[1:-1])
def val_func_replace(grid,val_func_replacee,val_func_replacer):return tuple(tuple(val_func_replacer if A==val_func_replacee else A for A in A)for A in grid)
def val_func_vsplit(grid,n):A=grid;B,D=len(A)//n,len(A[0]);E=len(A)%n!=0;return tuple(val_func_crop(A,(B*C+C*E,0),(B,D))for C in range(n))
def val_func_hsplit(grid,n):A=grid;D,B=len(A),len(A[0])//n;E=len(A[0])%n!=0;return tuple(val_func_crop(A,(0,B*C+C*E),(D,B))for C in range(n))
def val_func_subgrid(patch,grid):A=patch;return val_func_crop(grid,val_func_ulcorner(A),val_func_shape(A))
def val_func_paint(grid,obj):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(G,(C,D))in obj:
		if 0<=C<E and 0<=D<F:B[C][D]=G
	return tuple(tuple(A)for A in B)
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
def val_func_normalize(patch):
	A=patch
	if len(A)==0:return A
	return val_func_shift(A,(-val_func_uppermost(A),-val_func_leftmost(A)))
def val_func_shift(patch,directions):
	A=patch
	if len(A)==0:return A
	B,C=directions
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(D+B,E+C))for(A,(D,E))in A)
	return frozenset((A+B,D+C)for(A,D)in A)
def val_func_ulcorner(patch):return tuple(map(min,zip(*val_func_toindices(patch))))
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def val_func_colorfilter(objs,value):return frozenset(A for A in objs if next(iter(A))[0]==value)
def val_func_portrait(piece):A=piece;return val_func_height(A)>val_func_width(A)
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
def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_branch(condition,a,b):return a if condition else b
def val_func_last(container):return max(enumerate(container))[1]
def val_func_first(container):return next(iter(container))
def val_func_tojvec(j):return 0,j
def val_func_toivec(i):return i,0
def val_func_increment(x):return x+1 if isinstance(x,int)else(x[0]+1,x[1]+1)
def val_func_double(n):return n*2 if isinstance(n,int)else(n[0]*2,n[1]*2)
def val_func_invert(n):return-n if isinstance(n,int)else(-n[0],-n[1])
def p(I):I=tuple(map(tuple,I));H=val_func_objects(I,True,False,True);J=val_func_replace(I,5,0);K=val_func_colorfilter(H,2);L=val_func_first(K);A=val_func_portrait(L);M=val_func_branch(A,val_func_hsplit,val_func_vsplit);N=val_func_branch(A,val_func_vmirror,val_func_hmirror);B=val_func_ofcolor(I,2);O=val_func_subgrid(B,I);P=val_func_trim(O);Q=N(P);R=M(Q,2);S=val_func_compose(val_func_normalize,val_func_asobject);C=val_func_apply(S,R);D=val_func_last(C);T=val_func_first(C);U=val_func_ulcorner(B);E=val_func_increment(U);V=val_func_shift(D,E);W=val_func_shift(T,E);X=val_func_branch(A,val_func_width,val_func_height);Y=val_func_branch(A,val_func_tojvec,val_func_toivec);F=X(D);Z=val_func_double(F);G=val_func_compose(Y,val_func_increment);a=G(F);b=val_func_invert(a);c=G(Z);d=val_func_shift(V,b);e=val_func_shift(W,c);f=val_func_paint(J,d);g=val_func_paint(f,e);return[*map(list,g)]