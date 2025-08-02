def val_func_remove(value,container):A=container;return type(A)(A for A in A if A!=value)
def val_func_first(container):return next(iter(container))
def ival_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(loc):return val_func_dval_func_neighbors(loc)|ival_func_neighbors(loc)
def val_func_dval_func_neighbors(loc):A=loc;return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(grid):return frozenset((A,B)for A in range(len(grid))for B in range(len(grid[0])))
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
def val_func_mostcolor(element):A=element;B=[B for A in A for B in A]if isinstance(A,tuple)else[A for(A,B)in A];return max(set(B),key=B.count)
def val_func_index(grid,loc):
	B=loc;A=grid;C,D=B;E,F=len(A),len(A[0])
	if not(0<=C<E and 0<=D<F):return
	return A[B[0]][B[1]]
def val_func_toindices(patch):
	A=patch
	if len(A)==0:return frozenset()
	if isinstance(next(iter(A))[1],tuple):return frozenset(A for(B,A)in A)
	return A
def val_func_vmatching(a,b):return len(set(A for(B,A)in val_func_toindices(a))&set(A for(B,A)in val_func_toindices(b)))>0
def val_func_shift(patch,directions):
	A=patch
	if len(A)==0:return A
	B,C=directions
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(D+B,E+C))for(A,(D,E))in A)
	return frozenset((A+B,D+C)for(A,D)in A)
def val_func_shoot(start,direction):B=direction;A=start;return val_func_connect(A,(A[0]+42*B[0],A[1]+42*B[1]))
def val_func_gravitate(source,destination):
	D=destination;A=source;H,I=val_func_center(A);J,K=val_func_center(D);B,C=0,0
	if val_func_vmatching(A,D):B=1 if H<J else-1
	else:C=1 if I<K else-1
	E,F=B,C;G=0
	while not val_func_adjacent(A,D)and G<42:G+=1;E+=B;F+=C;A=val_func_shift(A,(B,C))
	return E-B,F-C
def val_func_cover(grid,patch):return val_func_fill(grid,val_func_mostcolor(grid),val_func_toindices(patch))
def val_func_connect(a,b):
	A,B=a;C,D=b;E=min(A,C);F=max(A,C)+1;G=min(B,D);H=max(B,D)+1
	if A==C:return frozenset((A,B)for B in range(G,H))
	elif B==D:return frozenset((A,B)for A in range(E,F))
	elif C-A==D-B:return frozenset((A,B)for(A,B)in zip(range(E,F),range(G,H)))
	elif C-A==B-D:return frozenset((A,B)for(A,B)in zip(range(E,F),range(H-1,G-1,-1)))
	return frozenset()
def val_func_center(patch):A=patch;return val_func_uppermost(A)+val_func_height(A)//2,val_func_leftmost(A)+val_func_width(A)//2
def val_func_replace(grid,val_func_replacee,val_func_replacer):return tuple(tuple(val_func_replacer if A==val_func_replacee else A for A in A)for A in grid)
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
def val_func_adjacent(a,b):return val_func_manhattan(a,b)==1
def val_func_manhattan(a,b):return min(abs(A-C)+abs(B-D)for(A,B)in val_func_toindices(a)for(C,D)in val_func_toindices(b))
def val_func_vline(patch):A=patch;return val_func_height(A)==len(A)and val_func_width(A)==1
def val_func_rightmost(patch):return max(A for(B,A)in val_func_toindices(patch))
def val_func_leftmost(patch):return min(A for(B,A)in val_func_toindices(patch))
def val_func_lowermost(patch):return max(A for(A,B)in val_func_toindices(patch))
def val_func_uppermost(patch):return min(A for(A,B)in val_func_toindices(patch))
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
def val_func_ofcolor(grid,value):return frozenset((A,C)for(A,B)in enumerate(grid)for(C,D)in enumerate(B)if D==value)
def val_func_colorfilter(objs,value):return frozenset(A for A in objs if next(iter(A))[0]==value)
def val_func_rbind(function,fixed):
	B=fixed;A=function;C=A.__code__.co_argcount
	if C==2:return lambda x:A(x,B)
	elif C==3:return lambda x,y:A(x,y,B)
	else:return lambda x,y,z:A(x,y,z,B)
def val_func_compose(outer,inner):return lambda x:outer(inner(x))
def val_func_branch(condition,a,b):return a if condition else b
def val_func_astuple(a,b):return a,b
def val_func_other(container,value):return val_func_first(val_func_remove(value,container))
def val_func_sfilter(container,condition):A=container;return type(A)(A for A in A if condition(A))
def val_func_crement(x):
	if isinstance(x,int):return 0 if x==0 else x+1 if x>0 else x-1
	return 0 if x[0]==0 else x[0]+1 if x[0]>0 else x[0]-1,0 if x[1]==0 else x[1]+1 if x[1]>0 else x[1]-1
def val_func_both(a,b):return a and b
def val_func_initset(value):return frozenset({value})
def val_func_argmax(container,compfunc):return max(container,key=compfunc)
def val_func_merge(containers):A=containers;return type(A)(B for A in A for B in A)
def val_func_greater(a,b):return a>b
def val_func_difference(a,b):return type(a)(A for A in a if A not in b)
def val_func_combine(a,b):return type(a)((*a,*b))
def val_func_subtract(a,b):
	if isinstance(a,int)and isinstance(b,int):return a-b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]-b[0],a[1]-b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a-b[0],a-b[1]
	return a[0]-b,a[1]-b
def val_func_add(a,b):
	if isinstance(a,int)and isinstance(b,int):return a+b
	elif isinstance(a,tuple)and isinstance(b,tuple):return a[0]+b[0],a[1]+b[1]
	elif isinstance(a,int)and isinstance(b,tuple):return a+b[0],a+b[1]
	return a[0]+b,a[1]+b
def p(I):M=False;I=tuple(map(tuple,I));D=val_func_ofcolor(I,2);A=val_func_ofcolor(I,3);N=val_func_vline(D);E=val_func_vline(A);B=val_func_center(D);G=val_func_branch(E,val_func_uppermost,val_func_rightmost);O=G(D);P=G(A);Q=val_func_greater(O,P);R=val_func_both(E,Q);S=val_func_branch(R,val_func_lowermost,val_func_uppermost);T=S(A);U=val_func_branch(E,val_func_leftmost,val_func_rightmost);V=U(A);C=val_func_astuple(T,V);W=val_func_other(A,C);X=val_func_subtract(C,W);Y=val_func_shoot(C,X);H=underval_func_fill(I,1,Y);Z=val_func_objects(H,True,M,M);J=val_func_colorfilter(Z,1);a=val_func_rbind(val_func_adjacent,A);b=val_func_sfilter(J,a);c=val_func_difference(J,b);d=val_func_merge(c);K=val_func_cover(H,d);e=val_func_shoot(B,(1,0));f=val_func_shoot(B,(-1,0));g=val_func_shoot(B,(0,-1));h=val_func_shoot(B,(0,1));i=val_func_combine(e,f);j=val_func_combine(g,h);k=val_func_branch(N,i,j);l=val_func_ofcolor(K,1);m=val_func_initset(C);n=val_func_rbind(val_func_manhattan,m);o=val_func_compose(n,val_func_initset);F=val_func_argmax(l,o);p=val_func_initset(F);q=val_func_gravitate(p,k);r=val_func_crement(q);L=val_func_add(F,r);s=val_func_connect(F,L);t=val_func_fill(K,1,s);u=val_func_connect(L,B);v=underval_func_fill(t,1,u);w=val_func_replace(v,1,3);return[*map(list,w)]