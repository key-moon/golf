def p(A):
	B=min(A for(A,B)in enumerate(A)for C in B if C==1);C=max(A for(A,B)in enumerate(A)for C in B if C==1);D=min(B for A in A for(B,C)in enumerate(A)if C==1);E=max(B for A in A for(B,C)in enumerate(A)if C==1);I=[A[D:E+1]for A in A[B:C+1]];J=(C-B)//2;K=(E-D)//2
	for(F,L)in enumerate(A):
		for(G,M)in enumerate(L):
			if M==4 and not(B<=F<=C and D<=G<=E):
				for(N,O)in enumerate(I):
					for(P,H)in enumerate(O):
						if H:A[F-J+N][G-K+P]=H
	return A