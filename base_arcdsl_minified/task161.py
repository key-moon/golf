def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_palette(A):
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
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
def val_func_mostcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_index(A,B):
	C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(A):
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_lrcorner(A):return tuple(map(max,zip(*val_func_toindices(A))))
def val_func_ulcorner(A):return tuple(map(min,zip(*val_func_toindices(A))))
def val_func_box(A):
	if len(A)==0:return A
	F,G=val_func_ulcorner(A);H,I=val_func_lrcorner(A);B,C=min(F,H),min(G,I);D,E=max(F,H),max(G,I);J={(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)};K={(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)};return frozenset(J|K)
def val_func_cover(A,B):return val_func_fill(A,val_func_mostcolor(A),val_func_toindices(B))
def val_func_connect(A,B):
	C,D=A;E,F=B;G=min(C,E);H=max(C,E)+1;I=min(D,F);J=max(D,F)+1
	if C==E:return frozenset((C,A)for A in range(I,J))
	elif D==F:return frozenset((A,D)for A in range(G,H))
	elif E-C==F-D:return frozenset((A,B)for(A,B)in zip(range(G,H),range(I,J)))
	elif E-C==D-F:return frozenset((A,B)for(A,B)in zip(range(G,H),range(J-1,I-1,-1)))
	return frozenset()
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_hline(A):return val_func_width(A)==len(A)and val_func_height(A)==1
def val_func_vline(A):return val_func_height(A)==len(A)and val_func_width(A)==1
def val_func_fgpartition(A):return frozenset(frozenset((A,(C,E))for(C,D)in enumerate(A)for(E,A)in enumerate(D)if A==B)for B in val_func_palette(A)-{val_func_mostcolor(A)})
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_leastcolor(A):B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return min(set(B),key=B.count)
def val_func_prapply(A,B,C):return frozenset(A(D,C)for C in C for D in B)
def val_func_fork(A,B,C):return lambda D:A(B(D),C(D))
def val_func_rbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(D,B)
	elif C==3:return lambda D,E:A(D,E,B)
	else:return lambda D,E,F:A(D,E,F,B)
def val_func_chain(A,B,C):return lambda D:A(B(C(D)))
def val_func_mfilter(A,B):return val_func_merge(val_func_sfilter(A,B))
def val_func_positive(A):return A>0
def val_func_either(A,B):return A or B
def val_func_both(A,B):return A and B
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_size(A):return len(A)
def val_func_difference(A,B):return type(A)(A for A in A if A not in B)
def p(A):A=tuple(map(tuple,A));B=val_func_leastcolor(A);C=val_func_ofcolor(A,B);E=val_func_prapply(val_func_connect,C,C);F=val_func_fgpartition(A);D=val_func_merge(F);G=val_func_cover(A,D);H=val_func_fork(val_func_either,val_func_hline,val_func_vline);I=val_func_box(D);J=val_func_rbind(val_func_difference,I);K=val_func_chain(val_func_positive,val_func_size,J);L=val_func_fork(val_func_both,H,K);M=val_func_mfilter(E,L);N=val_func_fill(G,B,M);return[*map(list,N)]