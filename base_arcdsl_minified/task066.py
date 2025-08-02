def val_func_remove(A,B):return type(B)(B for B in B if B!=A)
def val_func_first(A):return next(iter(A))
def val_func_ival_func_neighbors(A):return frozenset({(A[0]-1,A[1]-1),(A[0]-1,A[1]+1),(A[0]+1,A[1]-1),(A[0]+1,A[1]+1)})
def val_func_neighbors(A):return val_func_dval_func_neighbors(A)|val_func_ival_func_neighbors(A)
def val_func_dval_func_neighbors(A):return frozenset({(A[0]-1,A[1]),(A[0]+1,A[1]),(A[0],A[1]-1),(A[0],A[1]+1)})
def val_func_asindices(A):return frozenset((B,C)for B in range(len(A))for C in range(len(A[0])))
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
def val_func_vmatching(A,B):return len(set(A for(B,A)in val_func_toindices(A))&set(A for(B,A)in val_func_toindices(B)))>0
def val_func_shift(A,B):
	if len(A)==0:return A
	C,D=B
	if isinstance(next(iter(A))[1],tuple):return frozenset((A,(B+C,E+D))for(A,(B,E))in A)
	return frozenset((A+C,B+D)for(A,B)in A)
def val_func_shoot(A,B):return val_func_connect(A,(A[0]+42*B[0],A[1]+42*B[1]))
def val_func_gravitate(A,B):
	H,I=val_func_center(A);J,K=val_func_center(B);C,D=0,0
	if val_func_vmatching(A,B):C=1 if H<J else-1
	else:D=1 if I<K else-1
	E,F=C,D;G=0
	while not val_func_adjacent(A,B)and G<42:G+=1;E+=C;F+=D;A=val_func_shift(A,(C,D))
	return E-C,F-D
def val_func_cover(A,B):return val_func_fill(A,val_func_mostcolor(A),val_func_toindices(B))
def val_func_connect(A,B):
	C,D=A;E,F=B;G=min(C,E);H=max(C,E)+1;I=min(D,F);J=max(D,F)+1
	if C==E:return frozenset((C,A)for A in range(I,J))
	elif D==F:return frozenset((A,D)for A in range(G,H))
	elif E-C==F-D:return frozenset((A,B)for(A,B)in zip(range(G,H),range(I,J)))
	elif E-C==D-F:return frozenset((A,B)for(A,B)in zip(range(G,H),range(J-1,I-1,-1)))
	return frozenset()
def val_func_center(A):return val_func_uppermost(A)+val_func_height(A)//2,val_func_leftmost(A)+val_func_width(A)//2
def val_func_replace(A,B,C):return tuple(tuple(C if A==B else A for A in A)for A in A)
def underval_func_fill(A,B,C):
	G,H=len(A),len(A[0]);I=val_func_mostcolor(A);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:
			if D[E][F]==I:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_fill(A,B,C):
	G,H=len(A),len(A[0]);D=list(list(A)for A in A)
	for(E,F)in val_func_toindices(C):
		if 0<=E<G and 0<=F<H:D[E][F]=B
	return tuple(tuple(A)for A in D)
def val_func_adjacent(A,B):return val_func_manhattan(A,B)==1
def val_func_manhattan(A,B):return min(abs(A-D)+abs(C-E)for(A,C)in val_func_toindices(A)for(D,E)in val_func_toindices(B))
def val_func_vline(A):return val_func_height(A)==len(A)and val_func_width(A)==1
def val_func_rightmost(A):return max(A for(B,A)in val_func_toindices(A))
def val_func_leftmost(A):return min(A for(B,A)in val_func_toindices(A))
def val_func_lowermost(A):return max(A for(A,B)in val_func_toindices(A))
def val_func_uppermost(A):return min(A for(A,B)in val_func_toindices(A))
def val_func_objects(A,B,C,D):
	K=val_func_mostcolor(A)if D else None;L=set();G=set();O,P=len(A),len(A[0]);Q=val_func_asindices(A);R=val_func_neighbors if C else val_func_dval_func_neighbors
	for E in Q:
		if E in G:continue
		H=A[E[0]][E[1]]
		if H==K:continue
		M={(H,E)};I={E}
		while len(I)>0:
			N=set()
			for F in I:
				J=A[F[0]][F[1]]
				if H==J if B else J!=K:M.add((J,F));G.add(F);N|={(A,B)for(A,B)in R(F)if 0<=A<O and 0<=B<P}
			I=N-G
		L.add(frozenset(M))
	return frozenset(L)
def val_func_ofcolor(A,B):return frozenset((A,D)for(A,C)in enumerate(A)for(D,E)in enumerate(C)if E==B)
def val_func_colorfilter(A,B):return frozenset(A for A in A if next(iter(A))[0]==B)
def val_func_rbind(A,B):
	C=A.__code__.co_argcount
	if C==2:return lambda D:A(D,B)
	elif C==3:return lambda D,E:A(D,E,B)
	else:return lambda D,E,F:A(D,E,F,B)
def val_func_compose(A,B):return lambda C:A(B(C))
def val_func_branch(A,B,C):return B if A else C
def val_func_astuple(A,B):return A,B
def val_func_other(A,B):return val_func_first(val_func_remove(B,A))
def val_func_sfilter(A,B):return type(A)(A for A in A if B(A))
def val_func_crement(A):
	if isinstance(A,int):return 0 if A==0 else A+1 if A>0 else A-1
	return 0 if A[0]==0 else A[0]+1 if A[0]>0 else A[0]-1,0 if A[1]==0 else A[1]+1 if A[1]>0 else A[1]-1
def val_func_both(A,B):return A and B
def val_func_initset(A):return frozenset({A})
def val_func_argmax(A,B):return max(A,key=B)
def val_func_merge(A):return type(A)(B for A in A for B in A)
def val_func_greater(A,B):return A>B
def val_func_difference(A,B):return type(A)(A for A in A if A not in B)
def val_func_combine(A,B):return type(A)((*A,*B))
def val_func_subtract(A,B):
	if isinstance(A,int)and isinstance(B,int):return A-B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]-B[0],A[1]-B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A-B[0],A-B[1]
	return A[0]-B,A[1]-B
def val_func_add(A,B):
	if isinstance(A,int)and isinstance(B,int):return A+B
	elif isinstance(A,tuple)and isinstance(B,tuple):return A[0]+B[0],A[1]+B[1]
	elif isinstance(A,int)and isinstance(B,tuple):return A+B[0],A+B[1]
	return A[0]+B,A[1]+B
def p(A):M=False;A=tuple(map(tuple,A));E=val_func_ofcolor(A,2);B=val_func_ofcolor(A,3);N=val_func_vline(E);F=val_func_vline(B);C=val_func_center(E);H=val_func_branch(F,val_func_uppermost,val_func_rightmost);O=H(E);P=H(B);Q=val_func_greater(O,P);R=val_func_both(F,Q);S=val_func_branch(R,val_func_lowermost,val_func_uppermost);T=S(B);U=val_func_branch(F,val_func_leftmost,val_func_rightmost);V=U(B);D=val_func_astuple(T,V);W=val_func_other(B,D);X=val_func_subtract(D,W);Y=val_func_shoot(D,X);I=underval_func_fill(A,1,Y);Z=val_func_objects(I,True,M,M);J=val_func_colorfilter(Z,1);a=val_func_rbind(val_func_adjacent,B);b=val_func_sfilter(J,a);c=val_func_difference(J,b);d=val_func_merge(c);K=val_func_cover(I,d);e=val_func_shoot(C,(1,0));f=val_func_shoot(C,(-1,0));g=val_func_shoot(C,(0,-1));h=val_func_shoot(C,(0,1));i=val_func_combine(e,f);j=val_func_combine(g,h);k=val_func_branch(N,i,j);l=val_func_ofcolor(K,1);m=val_func_initset(D);n=val_func_rbind(val_func_manhattan,m);o=val_func_compose(n,val_func_initset);G=val_func_argmax(l,o);p=val_func_initset(G);q=val_func_gravitate(p,k);r=val_func_crement(q);L=val_func_add(G,r);s=val_func_connect(G,L);t=val_func_fill(K,1,s);u=val_func_connect(L,C);v=underval_func_fill(t,1,u);w=val_func_replace(v,1,3);return[*map(list,w)]