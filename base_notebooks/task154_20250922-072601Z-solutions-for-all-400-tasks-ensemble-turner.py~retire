def p(g):
	J,K=len(g),len(g[0]);C=[A[:]for A in g]
	def W():
		D=set();H=[]
		for E in range(J):
			for F in range(K):
				if C[E][F]==2 and(E,F)not in D:
					G=[(E,F)];D.add((E,F));I=[]
					while G:
						L,M=G.pop();I.append((L,M))
						for(N,O)in[(1,0),(-1,0),(0,1),(0,-1)]:
							A,B=L+N,M+O
							if 0<=A<J and 0<=B<K and C[A][B]==2 and(A,B)not in D:D.add((A,B));G.append((A,B))
					H.append(I)
		return H
	N=W()
	if len(N)!=2:return[A[:]for A in g]
	P=lambda c:(min(A for(A,B)in c),min(A for(B,A)in c),max(A for(A,B)in c),max(A for(B,A)in c));D,E=P(N[0]),P(N[1]);Q,R=((D[0]+D[2])/2,(D[1]+D[3])/2),((E[0]+E[2])/2,(E[1]+E[3])/2)
	if abs(Q[0]-R[0])>abs(Q[1]-R[1]):
		X,Y=(D,E)if D[0]<E[0]else(E,D);H,I=X[2]+1,Y[0]-1;S,L,M=[],[],[]
		for A in range(J):
			F=[B for B in range(K)if C[A][B]==5]
			if F:
				if A<H:S.append((A,F))
				elif A>I:M.append((A,F))
				else:L.append((A,F))
		for A in range(J):
			for B in range(K):
				if C[A][B]==5:C[A][B]=0
		A=H
		for(O,F)in sorted(S,reverse=1):
			if A>I:break
			for B in F:C[A][B]=5
			A+=1
		for(T,F)in L:
			if H<=T<=I:
				for B in F:C[T][B]=5
		A=I
		for(O,F)in sorted(M):
			if A<H:break
			for B in F:C[A][B]=5
			A-=1
	else:
		Z,a=(D,E)if D[1]<E[1]else(E,D);H,I=Z[3]+1,a[1]-1;M,L,U=[],[],[]
		for B in range(K):
			G=[A for A in range(J)if C[A][B]==5]
			if G:
				if B<H:M.append((B,G))
				elif B>I:U.append((B,G))
				else:L.append((B,G))
		for A in range(J):
			for B in range(K):
				if C[A][B]==5:C[A][B]=0
		B=H
		for(O,G)in sorted(M,reverse=1):
			if B>I:break
			for A in G:C[A][B]=5
			B+=1
		for(V,G)in L:
			if H<=V<=I:
				for A in G:C[A][V]=5
		B=I
		for(O,G)in sorted(U):
			if B<H:break
			for A in G:C[A][B]=5
			B-=1
	return[A[:]for A in C]