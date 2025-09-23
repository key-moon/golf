TWO,THREE=2,3
def _mostcolor(grid):
	A={}
	for C in grid:
		for B in C:A[B]=A.get(B,0)+1
	return max(A,key=A.get)
def _objects(grid):
	A=grid;I,J=len(A),len(A[0]);L=_mostcolor(A);F=[[False]*J for A in range(I)];M=[]
	for G in range(I):
		for H in range(J):
			if F[G][H]or A[G][H]==L:continue
			K=[(G,H)];F[G][H]=True;N=[]
			while K:
				B,C=K.pop();O=A[B][C];N.append((O,(B,C)))
				for(D,E)in((B-1,C),(B+1,C),(B,C-1),(B,C+1)):
					if 0<=D<I and 0<=E<J and not F[D][E]and A[D][E]!=L:F[D][E]=True;K.append((D,E))
			M.append(N)
	return M
def _to_indices(patch):
	A=patch
	if not A:return[]
	B=next(iter(A))
	if isinstance(B,tuple)and len(B)==2 and isinstance(B[1],tuple):return[A for(B,A)in A]
	return list(A)
def _bbox_stats(patch):A=_to_indices(patch);B=[A for(A,B)in A];C=[A for(B,A)in A];return min(B),max(B),min(C),max(C)
def _height(patch):
	A=patch
	if not A:return 0
	B,C,D,D=_bbox_stats(A);return C-B+1
def _width(patch):
	A=patch
	if not A:return 0
	B,B,C,D=_bbox_stats(A);return D-C+1
def _uppermost(patch):B,A,A,A=_bbox_stats(patch);return B
def _lowermost(patch):A,B,A,A=_bbox_stats(patch);return B
def _leftmost(patch):A,A,B,A=_bbox_stats(patch);return B
def _rightmost(patch):A,A,A,B=_bbox_stats(patch);return B
def _vline(patch):
	A=_to_indices(patch)
	if not A:return False
	return _width(A)==1 and _height(A)==len(A)
def _connect(a,b):
	A,B=a;C,D=b;E,F=min(A,C),max(A,C)+1;G,H=min(B,D),max(B,D)+1
	if A==C:return{(A,B)for B in range(G,H)}
	if B==D:return{(A,B)for A in range(E,F)}
	if C-A==D-B:return{(A,B)for(A,B)in zip(range(E,F),range(G,H))}
	if C-A==B-D:return{(A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1))}
	return set()
def _shoot(start,direction):B=direction;A=start;return _connect(A,(A[0]+42*B[0],A[1]+42*B[1]))
def _fill(grid,value,indices):
	A=grid;E,F=len(A),len(A[0]);B=[list(A)for A in A]
	for(C,D)in _to_indices(indices):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return B
def _underfill(grid,value,indices):
	A=grid;E,F=len(A),len(A[0]);G=_mostcolor(A);B=[list(A)for A in A]
	for(C,D)in _to_indices(indices):
		if 0<=C<E and 0<=D<F and B[C][D]==G:B[C][D]=value
	return B
def solve_b527c5c6(I):
	F=_objects(I);D=[]
	for B in F:
		A={B for(A,B)in B if A==TWO}
		if not A:continue
		J=_lowermost(A)==_lowermost(B);K=_rightmost(A)==_rightmost(B);L=_uppermost(A)==_uppermost(B);M=_leftmost(A)==_leftmost(B);N=(1 if J else 0)+(-1 if L else 0);O=(1 if K else 0)+(-1 if M else 0);P=_uppermost(A)+_height(A)//2;Q=_leftmost(A)+_width(A)//2;C=_shoot((P,Q),(N,O));D.append(C)
	R={B for A in D for B in A};S=_fill(I,TWO,R);E=set()
	for(B,C)in zip(F,D):
		T=_vline(C);G=min(_height(B),_width(B))
		for H in range(-(G-1),G):
			if T:E.update({(A,B+H)for(A,B)in C})
			else:E.update({(A+H,B)for(A,B)in C})
	return _underfill(S,THREE,E)
def p(g):return solve_b527c5c6(g)