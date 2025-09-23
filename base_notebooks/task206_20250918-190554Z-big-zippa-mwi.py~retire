def p(g):
	K=None;H,I=len(g),len(g[0]);from collections import Counter as V,deque;M=V(B for A in g for B in A).most_common(1)[0][0];J=[[False]*I for A in range(H)];N=[]
	for A in range(H):
		for B in range(I):
			if g[A][B]==M or J[A][B]:continue
			L=deque([(A,B)]);J[A][B]=True;C=[]
			while L:
				O,P=L.popleft();C.append((O,P))
				for(W,X)in((1,0),(-1,0),(0,1),(0,-1)):
					E,F=O+W,P+X
					if 0<=E<H and 0<=F<I and not J[E][F]and g[E][F]!=M:J[E][F]=True;L.append((E,F))
			N.append(C)
	D=K;G=K
	for C in N:
		if any(g[A][B]==5 for(A,B)in C):D=C
		else:G=C
	if D is K or G is K:return[A[:]for A in g]
	Q=min(A for(A,B)in D);R=min(A for(B,A)in D);Y=max(A for(A,B)in D);Z=max(A for(B,A)in D);a=Q+(Y-Q)//2;b=R+(Z-R)//2;c=min(A for(A,B)in G);d=min(A for(B,A)in G);S=[A[:]for A in g]
	for(A,B)in G:
		T=A-c+a-1;U=B-d+b-1
		if 0<=T<H and 0<=U<I:S[T][U]=g[A][B]
	return S