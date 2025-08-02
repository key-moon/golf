def p(A):
	D=len(A);E=len(A[0]);I=0
	for B in range(D):
		for C in range(E):
			F=A[B][C]
			if F:
				for G in range(B,D):
					for H in range(C,E):
						J=(G-B+1)*(H-C+1)
						if J>I and all(A[B][D]==F for B in range(B,G+1)for D in range(C,H+1)):I=J;L,M,N,O,P=B,C,G,H,F
	K=[[0]*E for A in range(D)]
	for Q in range(L,N+1):
		for R in range(M,O+1):K[Q][R]=P
	return K