def p(A):
	L,M=len(A),len(A[0]);C={}
	for(N,O)in enumerate(A):
		for(P,B)in enumerate(O):
			if B:C.setdefault(B,[]).append((N,P))
	E=[[0]*M for A in range(L)]
	for(Q,F)in C.items():
		if len(F)==1:
			G,B=F[0]
			for(R,D)in C.items():
				if len(D)==4:
					H=sum(A==G for(A,B)in D);I=sum(A==B for(C,A)in D)
					if H and I and H+I==4:
						for(J,K)in((0,0),(-1,0),(1,0),(0,-1),(0,1)):E[G+J][B+K]=R if J|K else Q
	return E