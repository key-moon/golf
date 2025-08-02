def p(val_g):
	A=val_g;F=next(A for B in A for A in B if A);B=[B for(B,A)in enumerate(A)if A.count(F)>len(A)/2];G=len(A[0]);C=[B for B in range(G)if sum(A[B]==F for A in A)>len(A)/2];B=[-1]+B+[len(A)];C=[-1]+C+[G]
	for D in range(len(B)-1):
		for E in range(len(C)-1):
			J=3 if(D+E)%2==0 else 4
			for H in range(B[D]+1,B[D+1]):
				for I in range(C[E]+1,C[E+1]):
					if A[H][I]==0:A[H][I]=J
	return A