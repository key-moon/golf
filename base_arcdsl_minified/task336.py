def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
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
def val_func_center(patch):A=patch;return val_func_uppermost(A)+val_func_height(A)//2,val_func_leftmost(A)+val_func_width(A)//2
def val_func_backdrop(patch):
	A=patch
	if len(A)==0:return frozenset({})
	B=val_func_toindices(A);C,D=val_func_ulcorner(B);E,F=val_func_lrcorner(A);return frozenset((A,B)for A in range(C,E+1)for B in range(D,F+1))
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
def val_func_connect(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def val_func_shoot(start,direction):B=direction;A=start;return val_func_connect(A,(A[0]+42*B[0],A[1]+42*B[1]))
def val_func_box(patch):
	A=patch
	if len(A)==0:return A
	F,G=val_func_ulcorner(A);H,I=val_func_lrcorner(A);B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def val_func_delta(patch):
	A=patch
	if len(A)==0:return frozenset({})
	return val_func_backdrop(A)-val_func_toindices(A)
def val_func_position(a,b):
	A,B=val_func_center(val_func_toindices(a));C,D=val_func_center(val_func_toindices(b))
	if A==C:return 0,1 if B<D else-1
	elif B==D:return 1 if A<C else-1,0
	elif A<C:return 1,1 if B<D else-1
	elif A>C:return-1,1 if B<D else-1
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def val_func_first(container):return next(iter(container))
def val_func_difference(a,b):return type(a)(A for A in a if A not in b)
def p(I):I=tuple(map(tuple,I));A=val_func_ofcolor(I,5);D=val_func_delta(A);E=val_func_fill(I,8,D);B=val_func_box(A);C=val_func_difference(B,A);F=val_func_position(B,C);G=val_func_first(C);H=val_func_shoot(G,F);J=val_func_fill(E,8,H);return[*map(list,J)]