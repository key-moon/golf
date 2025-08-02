def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_height(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A)
	return val_func_lowermost(A)-val_func_uppermost(A)+1
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_dmirror(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_frontiers(A):C,D=len(A),len(A[0]);B=tuple(A for(A,B)in enumerate(A)if len(set(B))==1);E=tuple(A for(A,B)in enumerate(val_func_dmirror(A))if len(set(B))==1);F=frozenset({frozenset({(A[B][C],(B,C))for C in range(D)})for B in B});G=frozenset({frozenset({(A[C][B],(C,B))for C in range(C)})for B in E});return F|G
def val_func_canvas(A,B):return tuple(tuple(A for B in range(B[1]))for C in range(B[0]))
def val_func_vline(A):return val_func_height(A)==len(A)and val_func_width(A)==1
def val_func_mostcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_astuple(A,B):return A,B
def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_increment(A):return A+1 if isinstance(A,int)else(A[0]+1,A[1]+1)
def val_func_size(A):return len(A)
def val_func_difference(A,B):return type(A)(A for A in A if A not in B)
def p(A):A=tuple(map(tuple,A));D=val_func_mostcolor(A);B=val_func_frontiers(A);C=val_func_sfilter(B,val_func_vline);E=val_func_difference(B,C);F=val_func_astuple(E,C);G=val_func_apply(val_func_size,F);H=val_func_increment(G);I=val_func_canvas(D,H);return[*map(list,I)]