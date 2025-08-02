def p(g):
	B=[(A,B)for A in range(len(g))for B in range(len(g[0]))if g[A][B]];C,L=min(A for(A,B)in B),max(A for(A,B)in B);D,M=min(A for(B,A)in B),max(A for(B,A)in B);A=[A[D:M+1]for A in g[C:L+1]];N=[(B,C)for B in range(len(A))for C in range(len(A[0]))if A[B][C]==4];H,I=N[0];O,P=len(A),len(A[0])
	for E in range(len(g)):
		for F in range(len(g[0])):
			if g[E][F]==4 and not(C+H==E and D+I==F):
				Q,R=E-(C+H),F-(D+I)
				for J in range(O):
					for K in range(P):
						G=A[J][K]
						if G:g[Q+J][R+K]=G if G==4 else 1
	return g