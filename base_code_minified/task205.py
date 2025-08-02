def p(A):
	G,H=len(A),len(A[0]);I=0
	for B in range(G):
		for D in range(B,G):
			for C in range(H):
				for E in range(C,H):
					J=(D-B+1)*(E-C+1)
					if J<=I:continue
					K={A[B][D]for B in range(B,D+1)for D in range(C,E+1)}
					if len(K)!=2:continue
					for L in K:
						F={(B,D)for B in range(B,D+1)for D in range(C,E+1)if A[B][D]==L};M={A for(A,B)in F};N={A for(B,A)in F}
						if F=={(A,B)for A in M for B in range(C,E+1)}|{(A,B)for A in range(B,D+1)for B in N}:I=J;O,P,Q,R=B,D,C,E
	return[[A[B][C]for C in range(Q,R+1)]for B in range(O,P+1)]