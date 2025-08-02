def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
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
def val_func_ulcorner(patch):return tuple(map(min,zip(*val_func_toindices(patch))))
def val_func_crop(grid,start,dims):A=start;return tuple(B[A[1]:A[1]+dims[1]]for B in grid[A[0]:A[0]+dims[0]])
def val_func_canvas(value,dimensions):A=dimensions;return tuple(tuple(value for A in range(A[1]))for B in range(A[0]))
def val_func_hsplit(grid,n):A=grid;D,B=len(A),len(A[0])//n;E=len(A[0])%n!=0;return tuple(val_func_crop(A,(0,B*C+C*E),(D,B))for C in range(n))
def val_func_vconcat(a,b):return a+b
def val_func_hconcat(a,b):return tuple(A+B for(A,B)in zip(a,b))
def val_func_vmirror(piece):
	A=piece
	if isinstance(A,tuple):return tuple(A[::-1]for A in A)
	B=val_func_ulcorner(A)[1]+val_func_lrcorner(A)[1]
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(C,B-D))for(A,(C,D))in A)
	return frozenset((A,B-C)for(A,C)in A)
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def val_func_height(piece):
	A=piece
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def val_func_astuple(a,b):return a,b
def val_func_last(container):return max(enumerate(container))[1]
def val_func_first(container):return next(iter(container))
def val_func_decrement(x):return x-1 if isinstance(x,int)else(x[0]-1,x[1]-1)
def val_func_subtract(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def p(I):I=tuple(map(tuple,I));C=val_func_ofcolor(I,5);D=val_func_ofcolor(I,8);E=val_func_height(C);F=val_func_decrement(E);G=val_func_height(D);A=val_func_subtract(F,G);H=val_func_astuple(1,A);J=val_func_canvas(8,H);K=val_func_subtract(6,A);L=val_func_astuple(1,K);M=val_func_canvas(0,L);N=val_func_hconcat(J,M);B=val_func_hsplit(N,2);O=val_func_first(B);P=val_func_last(B);Q=val_func_vmirror(P);R=val_func_vconcat(O,Q);S=val_func_astuple(1,3);T=val_func_canvas(0,S);U=val_func_vconcat(R,T);return[*map(list,U)]