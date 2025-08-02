def p(A):
	I=set();O=[];P=[];Q,R=len(A),len(A[0])
	for F in range(Q):
		for G in range(R):
			M=A[F][G]
			if M==1 and(F,G)not in I:
				H=J=F;K=L=G;N=[(F,G)];I.add((F,G))
				while N:
					D,E=N.pop()
					if D<H:H=D
					if D>J:J=D
					if E<K:K=E
					if E>L:L=E
					for S in(1,-1):
						B,C=D+S,E
						if 0<=B<Q and A[B][C]==1 and(B,C)not in I:I.add((B,C));N.append((B,C))
						B,C=D,E+S
						if 0<=C<R and A[B][C]==1 and(B,C)not in I:I.add((B,C));N.append((B,C))
				O.append((H,J,K,L))
			elif M>1:P.append((F,G,M))
	for(F,G,M)in P:
		for(H,J,K,L)in O:
			if H<=F<=J and K<=G<=L:
				T=H-1 if H else 0
				for D in range(T,J+1):
					for E in range(K,L+1):
						if A[D][E]==0:A[D][E]=M
				break
	return A