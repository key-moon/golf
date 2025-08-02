def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_mostcolor(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_connect(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def val_func_shoot(start,direction):B=direction;A=start;return val_func_connect(A,(A[0]+42*B[0],A[1]+42*B[1]))
def val_func_underfill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);G=val_func_mostcolor(A);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:
			if B[C][D]==G:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_shift(patch,directions):
	A=patch
	if len(A)==0:return A
	B,C=directions
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(D+B,E+C))for(A,(D,E))in A)
	return frozenset((A+B,D+C)for(A,D)in A)
def val_func_urcorner(patch):return tuple(map(lambda ix:{0:min,1:max}[ix[0]](ix[1]),enumerate(zip(*val_func_toindices(patch)))))
def val_func_ulcorner(patch):return tuple(map(min,zip(*val_func_toindices(patch))))
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def val_func_leastcolor(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def val_func_combine(a,b):return type(a)((*a,*b))
def p(I):I=tuple(map(tuple,I));A=val_func_leastcolor(I);C=val_func_ofcolor(I,A);B=val_func_shift(C,(-1,0));D=val_func_ulcorner(B);E=val_func_urcorner(B);F=val_func_shoot(D,(-1,-1));G=val_func_shoot(E,(-1,1));H=val_func_combine(F,G);J=val_func_underfill(I,A,H);return[*map(list,J)]