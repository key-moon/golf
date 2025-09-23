def p(g):
	J=len(g);K=len(g[0]);C=[A[:]for A in g]
	def X():
		D=set();H=[]
		for E in range(J):
			for F in range(K):
				if C[E][F]==2 and(E,F)not in D:
					G=[(E,F)];D.add((E,F));I=[]
					while G:
						L,M=G.pop();I.append((L,M))
						for(N,O)in((1,0),(-1,0),(0,1),(0,-1)):
							A,B=L+N,M+O
							if 0<=A<J and 0<=B<K and C[A][B]==2 and(A,B)not in D:D.add((A,B));G.append((A,B))
					H.append(I)
		return H
	M=X()
	if len(M)!=2:return[A[:]for A in g]
	def O(comp):A=[A for(A,B)in comp];B=[A for(B,A)in comp];return min(A),min(B),max(A),max(B)
	D=O(M[0]);E=O(M[1]);P=(D[0]+D[2])/2.,(D[1]+D[3])/2.;Q=(E[0]+E[2])/2.,(E[1]+E[3])/2.;Y=abs(P[0]-Q[0])>abs(P[1]-Q[1])
	if Y:
		Z,a=(D,E)if D[0]<E[0]else(E,D);H=Z[2]+1;I=a[0]-1;R=[];L=[];S=[]
		for A in range(J):
			F=[B for B in range(K)if C[A][B]==5]
			if not F:continue
			if A<H:R.append((A,F))
			elif A>I:S.append((A,F))
			else:L.append((A,F))
		for A in range(J):
			for B in range(K):
				if C[A][B]==5:C[A][B]=0
		A=H
		for(N,F)in sorted(R,reverse=True):
			if A>I:break
			for B in F:C[A][B]=5
			A+=1
		for(T,F)in L:
			if H<=T<=I:
				for B in F:C[T][B]=5
		A=I
		for(N,F)in sorted(S):
			if A<H:break
			for B in F:C[A][B]=5
			A-=1
	else:
		b,c=(D,E)if D[1]<E[1]else(E,D);H=b[3]+1;I=c[1]-1;U=[];L=[];V=[]
		for B in range(K):
			G=[A for A in range(J)if C[A][B]==5]
			if not G:continue
			if B<H:U.append((B,G))
			elif B>I:V.append((B,G))
			else:L.append((B,G))
		for A in range(J):
			for B in range(K):
				if C[A][B]==5:C[A][B]=0
		B=H
		for(N,G)in sorted(U,reverse=True):
			if B>I:break
			for A in G:C[A][B]=5
			B+=1
		for(W,G)in L:
			if H<=W<=I:
				for A in G:C[A][W]=5
		B=I
		for(N,G)in sorted(V):
			if B<H:break
			for A in G:C[A][B]=5
			B-=1
	return[A[:]for A in C]