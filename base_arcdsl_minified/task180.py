def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_rot270(grid):return tuple(tuple(A[::-1])for A in zip(*grid[::-1]))[::-1]
def val_func_rot90(grid):return tuple(A for A in zip(*grid[::-1]))
def val_func_righthalf(grid):return val_func_rot270(val_func_bottomhalf(val_func_rot90(grid)))
def val_func_lefthalf(grid):return val_func_rot270(val_func_tophalf(val_func_rot90(grid)))
def val_func_bottomhalf(grid):A=grid;return A[len(A)//2+len(A)%2:]
def val_func_tophalf(grid):return grid[:len(grid)//2]
def val_func_paint(grid,obj):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(G,(C,D))in obj:
		if 0<=C<E and 0<=D<F:B[C][D]=G
	return tuple(tuple(A)for A in B)
def val_func_toobject(patch,grid):A=grid;D,E=len(A),len(A[0]);return frozenset((A[B][C],(B,C))for(B,C)in val_func_toindices(patch)if 0<=B<D and 0<=C<E)
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
def val_func_fork(outer,a,b):return lambda x:outer(a(x),b(x))
def val_func_rbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def val_func_difference(a,b):return type(a)(A for A in a if A not in b)
def val_func_identity(x):return x
def p(I):I=tuple(map(tuple,I));B=val_func_lefthalf(I);C=val_func_righthalf(I);D=val_func_tophalf(B);E=val_func_bottomhalf(B);F=val_func_tophalf(C);G=val_func_bottomhalf(C);H=val_func_rbind(val_func_ofcolor,0);J=val_func_fork(val_func_difference,val_func_asindices,H);A=val_func_fork(val_func_toobject,J,val_func_identity);K=A(F);L=A(E);M=A(G);N=val_func_paint(D,M);O=val_func_paint(N,L);P=val_func_paint(O,K);return[*map(list,P)]