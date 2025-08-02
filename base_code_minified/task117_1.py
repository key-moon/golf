def p(A):
	F,G=len(A),len(A[0]);H=list({A for B in A for A in B if A});I={}
	for J in H:
		K=L=0
		for(B,D)in enumerate(A):
			for(C,E)in enumerate(D):
				if E==J:M=2*B-(F-1);N=2*C-(G-1);L+=M*M+N*N;K+=1
		I[J]=L/K
	O=max(H,key=lambda F:I[F]);P=[A[:]for A in A]
	for(B,D)in enumerate(A):
		for(C,E)in enumerate(D):
			if E==O:
				for Q in(B,F-1-B):
					for R in(C,G-1-C):P[Q][R]=O
	return P