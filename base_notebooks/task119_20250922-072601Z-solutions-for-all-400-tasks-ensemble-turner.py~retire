def p(g):
	E,C=len(g),len(g[0]);G=[A[:]for A in g];H=lambda gd,gv:gd[::-1]if gv>=2 else gd;H=lambda gd,gv:[list(A)for A in zip(*H(gd,gv))]if gv%2 else H(gd,gv);I=[(A,B)for A in range(E)for B in range(C)if g[A][B]==8]
	if not I:return G
	J,O=None,0
	for K in[0,1,2,3]:
		for P in[0,1]:
			for L in range(1,min(E//2,C//2)):
				for Q in range(C):
					A=[[0]*C for A in range(E)]
					for D in range(L):
						for B in range(C):A[D][B]=2
					R=len(I)
					for B in range(C):
						D=L+abs(Q-B)
						if 0<=D<E:A[D][B]=8 if B<R else 3
					if P:A=[A[::-1]for A in A]
					A=A[::-1]if K>=2 else A;A=[list(A)for A in zip(*A)]if K%2 else A;M=sum(1 for(B,C)in I if A[B][C]==8);N=[(A,B)for A in range(E)for B in range(C)if g[A][B]==2];S=sum(1 for(B,C)in N if A[B][C]==2);M+=S/len(N)if N else 0
					if M>O:O,J=M,(K,P,L,Q,R,A)
	if J:
		F,F,F,F,F,A=J
		for D in range(E):
			for B in range(C):
				if A[D][B]==3 and g[D][B]==0:G[D][B]=3
	return G