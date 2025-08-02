def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_shift(patch,directions):
	A=patch
	if len(A)==0:return A
	B,C=directions
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(D+B,E+C))for(A,(D,E))in A)
	return frozenset((A+B,D+C)for(A,D)in A)
def val_func_ulcorner(patch):return tuple(map(min,zip(*val_func_toindices(patch))))
def val_func_downscale(grid,factor):
	G=factor;C=grid;D,I=len(C),len(C[0]);A=tuple()
	for B in range(D):
		E=tuple()
		for H in range(I):
			if H%G==0:E=E+(C[B][H],)
		A=A+(E,)
	D=len(A);F=tuple()
	for B in range(D):
		if B%G==0:F=F+(A[B],)
	return F
def val_func_upscale(element,factor):
	B=element;A=factor
	if isinstance(B,tuple):
		C=tuple()
		for I in B:
			D=tuple()
			for E in I:D=D+tuple(E for A in range(A))
			C=C+tuple(D for A in range(A))
		return C
	else:
		if len(B)==0:return frozenset()
		F,G=val_func_ulcorner(B);J,K=-F,-G;L=val_func_shift(B,(J,K));H=set()
		for(E,(M,N))in L:
			for O in range(A):
				for P in range(A):H.add((E,(M*A+O,N*A+P)))
		return val_func_shift(frozenset(H),(F,G))
def val_func_rot180(grid):return tuple(tuple(A[::-1])for A in grid[::-1])
def p(I):I=tuple(map(tuple,I));A=val_func_rot180(I);B=val_func_downscale(A,2);C=val_func_rot180(B);D=val_func_upscale(C,4);return[*map(list,D)]