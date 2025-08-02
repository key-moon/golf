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
def val_func_tophalf(A):return A[:len(A)//2]
def val_func_bottomhalf(A):return A[len(A)//2+len(A)%2:]
def val_func_rot270(A):return tuple(tuple(A[::-1])for A in zip(*A[::-1]))[::-1]
def val_func_rot90(A):return tuple(A for A in zip(*A[::-1]))
def val_func_righthalf(A):return val_func_rot270(val_func_bottomhalf(val_func_rot90(A)))
def val_func_lefthalf(A):return val_func_rot270(val_func_tophalf(val_func_rot90(A)))
def val_func_replace(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def val_func_hconcat(A,B):return tuple(A+B for(A,B)in zip(A,B))
def val_func_dmirror(A):
	if isinstance(A,tuple):return tuple(zip(*A))
	B,C=val_func_ulcorner(A)
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(E-C+B,D-B+C))for(A,(D,E))in A)
	return frozenset((D-C+B,A-B+C)for(A,D)in A)
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_portrait(A):return val_func_height(A)>val_func_width(A)
def val_func_leastcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def val_func_apply(A,B):return type(B)(A(B)for B in B)
def val_func_rbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(D,B)
	elif C==3:return lambda D,E:A(D,E,B)
	else:return lambda D,E,F:A(D,E,F,B)
def val_func_branch(A,B,C):return B if A else C
def val_func_order(A,B):return tuple(sorted(A,key=B))
def val_func_invert(A):return-A if isinstance(A,int)else(-A[0],-A[1])
def val_func_identity(A):return A
def p(A):A=tuple(map(tuple,A));D=val_func_leastcolor(A);E=val_func_replace(A,D,5);F=val_func_ofcolor(A,5);G=val_func_portrait(F);B=val_func_branch(G,val_func_identity,val_func_dmirror);C=B(E);H=val_func_lefthalf(C);I=val_func_righthalf(C);J=val_func_rbind(val_func_order,val_func_identity);K=val_func_rbind(val_func_order,val_func_invert);L=val_func_apply(J,H);M=val_func_apply(K,I);N=val_func_hconcat(L,M);O=B(N);return[*map(list,O)]