def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def ival_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(loc):return val_func_dval_func_neighbors(loc)|ival_func_neighbors(loc)
def val_func_dval_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
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
def val_func_palette(element):
	A=element
	if isinstance(A,tuple):return frozenset({B for A in A for B in A})
	return frozenset({A for(A,B)in A})
def val_func_mostcolor(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_shoot(start,direction):B=direction;A=start;return val_func_connect(A,(A[0]+42*B[0],A[1]+42*B[1]))
def val_func_vfrontier(location):return frozenset((A,location[1])for A in range(30))
def val_func_connect(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def underval_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);G=val_func_mostcolor(A);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:
			if B[C][D]==G:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_fill(grid,value,patch):
	A=grid;E,F=len(A),len(A[0]);B=list(list(A)for A in A)
	for(C,D)in val_func_toindices(patch):
		if 0<=C<E and 0<=D<F:B[C][D]=value
	return tuple(tuple(A)for A in B)
def val_func_numcolors(element):return len(val_func_palette(element))
def val_func_vline(patch):A=patch;return val_func_height(A)==len(A)and val_func_width(A)==1
def val_func_objects(grid,univalued,diagonal,without_bg):
	A=grid;H=val_func_mostcolor(A)if without_bg else None;I=set();D=set();L,M=len(A),len(A[0]);N=val_func_asindices(A);O=val_func_neighbors if diagonal else val_func_dval_func_neighbors
	for B in N:
		if B in D:continue
		E=A[B[0]][B[1]]
		if E==H:continue
		J={(E,B)};F={B}
		while len(F)>0:
			K=set()
			for C in F:
				G=A[C[0]][C[1]]
				if E==G if univalued else G!=H:J.add((G,C));D.add(C);K|={(A,B)for(A,B)in O(C)if 0<=A<L and 0<=B<M}
			F=K-D
		I.add(frozenset(J))
	return frozenset(I)
def val_func_shift(patch,directions):
	A=patch
	if len(A)==0:return A
	B,C=directions
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(D+B,E+C))for(A,(D,E))in A)
	return frozenset((A+B,D+C)for(A,D)in A)
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_urcorner(patch):return tuple(map(lambda ix:{0:min,1:max}[ix[0]](ix[1]),enumerate(zip(*val_func_toindices(patch)))))
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def val_func_colorfilter(objs,value):return frozenset(A for A in objs if next(iter(A))[0]==value)
def val_func_prval_func_apply(function,a,b):return frozenset(function(B,A)for A in b for B in a)
def mval_func_apply(function,container):return val_func_merge(val_func_apply(function,container))
def val_func_apply(function,container):A=container;return type(A)(function(A)for A in A)
def val_func_rbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def val_func_matcher(function,target):return lambda x:function(x)==target
def val_func_mfilter(container,function):return val_func_merge(val_func_sfilter(container,function))
def val_func_sfilter(container,condition):A=container;return type(A)(A for A in A if condition(A))
def val_func_difference(a,b):return type(a)(A for A in a if A not in b)
def p(I):D=False;I=tuple(map(tuple,I));E=val_func_ofcolor(I,2);F=val_func_ofcolor(I,5);G=val_func_prval_func_apply(val_func_connect,E,F);H=val_func_mfilter(G,val_func_vline);A=underval_func_fill(I,2,H);J=val_func_matcher(val_func_numcolors,2);B=val_func_objects(A,D,D,True);C=val_func_sfilter(B,J);K=val_func_difference(B,C);L=val_func_colorfilter(K,2);M=mval_func_apply(val_func_toindices,L);N=val_func_apply(val_func_urcorner,C);O=val_func_shift(N,(1,1));P=val_func_rbind(val_func_shoot,(-1,0));Q=mval_func_apply(P,O);R=val_func_fill(A,2,Q);S=mval_func_apply(val_func_vfrontier,M);T=val_func_fill(R,2,S);return[*map(list,T)]