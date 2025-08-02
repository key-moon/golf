def p(A):
	C=A[0];D=[(A,B)for(B,A)in enumerate(C)if A];B=len(C)*len(D);A=[[0]*B for A in range(B)]
	for E in range(B):
		for(G,H)in D:
			F=H+E
			if F<B:A[B-1-E][F]=G
	return A