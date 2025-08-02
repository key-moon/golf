def p(g):
	K={}
	for(C,F)in enumerate(g):
		for(B,D)in enumerate(F):
			A=K.get(D)
			if A:A[0]+=1;A[1]=min(A[1],C);A[2]=max(A[2],C);A[3]=min(A[3],B);A[4]=max(A[4],B)
			else:K[D]=[1,C,C,B,B]
	L=M=0
	for(D,(N,G,H,I,J))in K.items():
		A=(H-G+1)*(J-I+1)
		if N==A>1 and A>M:M=A;L=D
	if M:
		G,H,I,J=K[L][1:]
		for(C,F)in enumerate(g):
			for(B,D)in enumerate(F):
				if D!=L:
					if G<=C<=H:
						if B<I:
							for E in range(B+1,I):F[E]=D
						elif B>J:
							for E in range(J+1,B):F[E]=D
					if I<=B<=J:
						if C<G:
							for E in range(C+1,G):g[E][B]=D
						elif C>H:
							for E in range(H+1,C):g[E][B]=D
	return g