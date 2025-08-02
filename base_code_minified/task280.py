def p(A):
	F,G=len(A),len(A[0])
	for H in range(F):
		for I in range(G):
			if A[H][I]==2:
				J=0
				for(B,C)in((-1,0),(1,0),(0,-1),(0,1)):
					D,E=H+B,I+C;K=0
					while 0<=D<F and 0<=E<G and A[D][E]==0:K+=1;D+=B;E+=C
					if K>J:J=K;O=B,C
				B,C=O
				for N in range(J+1):
					D,E=H+B*N,I+C*N;A[D][E]=2
					for(P,Q)in((-C,B),(C,-B)):
						L,M=D+P,E+Q
						if 0<=L<F and 0<=M<G and A[L][M]==0:A[L][M]=3
	return A