def p(g):
	F,G=len(g),len(g[0]);H=0
	for A in range(F):
		for C in range(A,F):
			for B in range(G):
				for D in range(B,G):
					I=(C-A+1)*(D-B+1)
					if I<=H:continue
					J={g[A][C]for A in range(A,C+1)for C in range(B,D+1)}
					if len(J)!=2:continue
					for K in J:
						E={(A,C)for A in range(A,C+1)for C in range(B,D+1)if g[A][C]==K};L={A for(A,B)in E};M={A for(B,A)in E}
						if E=={(A,C)for A in L for C in range(B,D+1)}|{(A,B)for A in range(A,C+1)for B in M}:H=I;N,O,P,Q=A,C,B,D
	return[[g[A][B]for B in range(P,Q+1)]for A in range(N,O+1)]