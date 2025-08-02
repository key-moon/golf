def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
def val_func_width(A):
	if len(A)==0:return 0
	if isinstance(A,tuple):return len(A[0])
	return val_func_rightmost(A)-val_func_leftmost(A)+1
def val_func_matcher(A,B):return lambda C:A(C)==B
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_last(A):return max(enumerate(A))[1]
def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_flip(A):return not A
def val_func_halve(A):return A//2 if isinstance(A,int)else(A[0]//2,A[1]//2)
def p(A):A=tuple(map(tuple,A));B=val_func_asindices(A);C=val_func_width(A);D=val_func_halve(C);E=val_func_matcher(val_func_last,D);F=val_func_compose(val_func_flip,E);G=val_func_sfilter(B,F);H=val_func_fill(A,0,G);return[*map(list,H)]