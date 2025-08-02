def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_hfrontier(location):return frozenset((location[0],A)for A in range(30))
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def val_func_mval_func_apply(function,container):return val_func_merge(val_func_apply(function,container))
def val_func_lbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda y:A(B,y)
	elif C==3:return lambda y,z:A(B,y,z)
	else:return lambda y,z,a:A(B,y,z,a)
def val_func_matcher(function,target):return lambda x:function(x)==target
def val_func_chain(h,g,f):return lambda x:h(g(f(x)))
def val_func_last(container):return max(enumerate(container))[1]
def val_func_sfilter(container,condition):A=container;return type(A)(A for A in A if condition(A))
def p(I):I=tuple(map(tuple,I));B=val_func_ofcolor(I,5);C=val_func_lbind(val_func_matcher,val_func_last);D=val_func_lbind(val_func_sfilter,B);E=val_func_lbind(val_func_mval_func_apply,val_func_hfrontier);A=val_func_chain(E,D,C);F=A(0);G=A(2);H=A(1);J=val_func_fill(I,2,F);K=val_func_fill(J,3,G);L=val_func_fill(K,4,H);return[*map(list,L)]