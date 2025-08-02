def p(A):
	B,R=len(A),len(A[0]);C=R;G=[[0]*C for A in range(B)]
	for H in range(B-1):
		for I in range(C-1):
			D=[A[H+B][I+C]for B in(0,1)for C in(0,1)]
			if D.count(2)==1 and(S:=set(D)-{2}):
				T=S.pop();U=D.index(2);J,K=divmod(U,2);L=-1 if J<1 else 1;M=-1 if K<1 else 1;N=[-M,L];E,F=H+J,I+K
				while 0<=E<B and 0<=F<C:
					for O in(-1,0,1):
						P,Q=E+N[0]*O,F+N[1]*O
						if 0<=P<B and 0<=Q<C:G[P][Q]=T
					E+=L;F+=M
				return G