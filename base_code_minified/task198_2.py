def p(A):
	G,J=len(A),len(A[0]);O=next(A for B in A for A in B if A);H=[B for B in range(G)if A[B].count(O)>J/2];I=[B for B in range(J)if sum(A[C][B]==O for C in range(G))>G/2];L=[-1]+H+[G];M=[-1]+I+[J];N,D=len(L)-1,len(M)-1;V=list(range(N*D))
	def K(A):
		while P[A]!=A:A=P[A]
		return A
	def Q(A,B):
		A,B=K(A),K(B)
		if A!=B:P[A]=B
	for E in H:
		B=sum(1 for A in H if A<E)
		for F in range(J):
			if A[E][F]==0 and F not in I:C=sum(1 for A in I if A<F);Q(B*D+C,(B+1)*D+C)
	for F in I:
		C=sum(1 for A in I if A<F)
		for E in range(G):
			if A[E][F]==0 and E not in H:B=sum(1 for A in H if A<E);Q(B*D+C,B*D+C+1)
	from collections import Counter as R;S=R(K(A)for A in range(N*D));T=S.most_common(1)[0][0]
	for B in range(N):
		for C in range(D):
			U=4 if K(B*D+C)==T else 3
			for E in range(L[B]+1,L[B+1]):
				for F in range(M[C]+1,M[C+1]):A[E][F]=U
	return A