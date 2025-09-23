_B=False
_A=True
def _normalize_pixels(pxs):
	A=pxs
	if not A:return set()
	B=[A for(B,(A,C))in A];C=[A for(B,(C,A))in A];D,E=min(B),min(C);return{(A,(B-D,C-E))for(A,(B,C))in A}
def _upscale_pixels(pxs,f):return{(A,(B*f+D,C*f+E))for(A,(B,C))in pxs for D in range(f)for E in range(f)}
def _outbox_indices(coords):
	A=coords
	if not A:return set()
	F=[A for(A,B)in A];G=[A for(B,A)in A];B,C=min(F)-1,min(G)-1;D,E=max(F)+1,max(G)+1;return{(A,C)for A in range(B,D+1)}|{(A,E)for A in range(B,D+1)}|{(B,A)for A in range(C,E+1)}|{(D,A)for A in range(C,E+1)}
def _occurrences(G,pattern):
	C=pattern
	if not C or not G or not G[0]:return set()
	D,E=len(G),len(G[0]);A=_normalize_pixels(C);N=[A for(B,(A,C))in A];O=[A for(B,(C,A))in A];P,Q=max(N)+1,max(O)+1;F=set()
	for H in range(-P+1,D):
		for I in range(-Q+1,E):
			B=_A;J=_B
			for(K,(R,S))in A:
				L,M=H+R,I+S
				if 0<=L<D and 0<=M<E:
					J=_A
					if G[L][M]!=K:B=_B;break
				elif K!=0:B=_B;break
			if B and J:F.add((H,I))
	return F
def _components_8(G,bg):
	if not G or not G[0]:return[]
	F,H=len(G),len(G[0]);C=[[_B]*H for A in range(F)];L=[];N=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)];from collections import deque
	for D in range(F):
		for E in range(H):
			if C[D][E]or G[D][E]==bg:continue
			I=deque([(D,E)]);C[D][E]=_A;M=[]
			while I:
				J,K=I.popleft();M.append((G[J][K],(J,K)))
				for(O,P)in N:
					A,B=J+O,K+P
					if 0<=A<F and 0<=B<H and not C[A][B]and G[A][B]!=bg:C[A][B]=_A;I.append((A,B))
			L.append(M)
	return L
def solve_447fd412(I):
	from collections import Counter as Q
	if not I or not I[0]:return[]
	C={}
	for R in I:
		for D in R:C[D]=C.get(D,0)+1
	S=max(C,key=C.get);E=_components_8(I,S)
	if not E:return I
	E.sort(key=lambda c:len({A for(A,B)in c}),reverse=_A);L=E[0];T=_normalize_pixels(L);U=Q(A for(A,B)in L);M=max(U.items(),key=lambda kv:(kv[1],-kv[0]))[0];F=[]
	for V in(1,2,3):
		G=_upscale_pixels(T,V);H={(A,B)for(A,B)in G if A!=M};B=set();A=set()
		if H:A={A for(B,A)in H};J=H|{(0,A)for A in _outbox_indices(A)};B=_occurrences(I,J)
		if not B:
			K={(A,B)for(A,B)in G if A==M}
			if not K:continue
			A={A for(B,A)in K};J=K|{(0,A)for A in _outbox_indices(A)};B=_occurrences(I,J)
		if not B:continue
		W=min(A for(A,B)in A);X=min(A for(B,A)in A)
		for(Y,Z)in B:a,b=Y-W+1,Z-X+1;F.append({(A,(B+a,C+b))for(A,(B,C))in G})
	if not F:return I
	c,d=len(I),len(I[0]);N=[list(A)for A in I]
	for(D,(O,P))in set().union(*F):
		if 0<=O<c and 0<=P<d:N[O][P]=D
	return tuple(tuple(A)for A in N)
def p(g):A=solve_447fd412(g);return[list(A)for A in A]