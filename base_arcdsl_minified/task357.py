def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
def val_func_lrcorner(patch):return tuple(map(max,zip(*val_func_toindices(patch))))
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_shape(piece):A=piece;return val_func_height(A),val_func_width(A)
def val_func_connect(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def val_func_shoot(start,direction):B=direction;A=start;return val_func_connect(A,(A[0]+42*B[0],A[1]+42*B[1]))
def val_func_replace(grid,val_func_replacee,val_func_replacer):return tuple(tuple(val_func_replacer if A==val_func_replacee else A for A in A)for A in grid)
def val_func_subgrid(patch,grid):A=patch;return val_func_crop(grid,val_func_ulcorner(A),val_func_shape(A))
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_hmirror(piece):
	A=piece
	if isinstance(A,tuple):return A[::-1]
	B=val_func_ulcorner(A)[0]+val_func_lrcorner(A)[0]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B-C,D))for(A,(C,D))in A)
	return frozenset((B-A,C)for(A,C)in A)
def val_func_crop(grid,start,dims):A=start;return tuple(B[A[1]:A[1]+dims[1]]for B in grid[A[0]:A[0]+dims[0]])
def val_func_urcorner(patch):return tuple(map(lambda ix:{0:min,1:max}[ix[0]](ix[1]),enumerate(zip(*val_func_toindices(patch)))))
def val_func_ulcorner(patch):return tuple(map(min,zip(*val_func_toindices(patch))))
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
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
def val_func_astuple(a,b):return a,b
def val_func_first(container):return next(iter(container))
def val_func_decrement(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_repeat(item,num):return tuple(item for A in range(num))
def p(I):I=tuple(map(tuple,I));F=val_func_height(I);G=val_func_ofcolor(I,1);H=val_func_first(G);J=val_func_shoot(H,(-1,1));B=val_func_fill(I,1,J);K=val_func_ofcolor(B,1);L=val_func_urcorner(K);M=val_func_shoot(L,(-1,-1));A=val_func_fill(B,1,M);C=val_func_ofcolor(A,1);D=val_func_subgrid(C,A);N=val_func_height(D);E=val_func_width(D);O=val_func_decrement(N);P=val_func_astuple(O,E);Q=val_func_ulcorner(C);R=val_func_crop(A,Q,P);S=val_func_repeat(R,9);T=val_func_merge(S);U=val_func_astuple(F,E);V=val_func_crop(T,(0,0),U);W=val_func_hmirror(V);X=val_func_replace(W,0,8);return[*map(list,X)]